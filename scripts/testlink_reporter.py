"""Registra resultados en TestLink por XML-RPC.
Lee reports/**/*.xml (JUnit) y reports/testlink.csv (id,herramienta,estado,mensaje).
Un test llamado test_cpNN_... se registra como <TL_PREFIX>-NN.
Variables: TL_URL, TL_API_KEY, TL_PLAN_ID, TL_PREFIX, PIPELINE_ID, REPORT_URL, TL_BUILD"""
import os, re, sys, glob, csv, datetime
import xmlrpc.client
import xml.etree.ElementTree as ET

URL = os.environ.get("TL_URL", "http://localhost:8082/lib/api/xmlrpc/v1/xmlrpc.php")
KEY = os.environ.get("TL_API_KEY", "")
PLAN = int(os.environ.get("TL_PLAN_ID", "0"))
PREFIX = os.environ.get("TL_PREFIX", "AN")
PIPE = os.environ.get("PIPELINE_ID", "local")
LINK = os.environ.get("REPORT_URL", "")
BUILD = os.environ.get("TL_BUILD", PIPE)
if not KEY or not PLAN:
    print("Falta TL_API_KEY o TL_PLAN_ID: no se registra nada")
    sys.exit(1)

items = []
for f in glob.glob("reports/**/*.xml", recursive=True):
    try:
        root = ET.parse(f).getroot()
    except ET.ParseError:
        continue
    for tc in root.iter("testcase"):
        m = re.search(r"cp[-_ ]?(\d+)", tc.get("name", "") + tc.get("classname", ""), re.I)
        if not m:
            continue
        st, msg = "p", ""
        for tag, code in (("failure", "f"), ("error", "f"), ("skipped", "b")):
            n = tc.find(tag)
            if n is not None:
                st, msg = code, (n.get("message") or "")[:500]
        items.append((f"{PREFIX}-{int(m.group(1))}", f, st, msg))
if os.path.exists("reports/testlink.csv"):
    for r in csv.reader(open("reports/testlink.csv", encoding="utf-8")):
        if len(r) >= 3:
            items.append((r[0], r[1], r[2], r[3] if len(r) > 3 else ""))

srv = xmlrpc.client.ServerProxy(URL)
errores = 0
for ext, tool, st, msg in items:
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notas = f"Herramienta: {tool}\nFecha: {ahora}\nPipeline: {PIPE}\nReporte: {LINK}\nError: {msg}"
    try:
        r = srv.tl.reportTCResult({"devKey": KEY, "testcaseexternalid": ext, "testplanid": PLAN,
                                   "buildname": BUILD, "status": st, "notes": notas, "overwrite": True})
        print(ext, st, "->", r[0].get("message", r[0]) if isinstance(r, list) and r else r)
    except Exception as e:
        errores += 1
        print("ERROR", ext, e)
print(f"Registrados: {len(items) - errores}/{len(items)}")
