"""Convierte los logs de k6 en reports/testlink.csv (id,herramienta,estado,mensaje)."""
import os, re, csv
OFFSET = {"rendimiento": ("rd", 41), "estres": ("es", 51), "seguridad": ("se", 61)}
PREFIX = os.environ.get("TL_PREFIX", "AN")
filas = []
for suite, (pre, off) in OFFSET.items():
    log = f"reports/{suite}.log"
    if not os.path.exists(log):
        continue
    cur = None
    for l in open(log, encoding="utf-8"):
        m = re.match(r"=== (\w\w)-(\d+)", l)
        if m:
            cur = {"id": f"{PREFIX}-{off + int(m.group(2))}", "code": None, "caido": False}
            filas.append(cur)
        elif cur and "código de salida:" in l:
            cur["code"] = l.split("código de salida:")[1].split()[0]
        elif cur and "servidor: CAÍDO" in l:
            cur["caido"] = True
with open("reports/testlink.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for c in filas:
        ok = c["code"] == "0" and not c["caido"]
        msg = "" if ok else f"Umbral incumplido (codigo {c['code']})" + (" - servidor caido" if c["caido"] else "")
        w.writerow([c["id"], "Grafana k6", "p" if ok else "f", msg])
print("Filas k6:", len(filas))
