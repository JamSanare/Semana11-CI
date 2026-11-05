"""Crea el build en TestLink (nombre = PIPELINE_ID) si no existe."""
import os, sys, xmlrpc.client
url = os.environ.get("TL_URL", "http://localhost:8082/lib/api/xmlrpc/v1/xmlrpc.php")
key, plan = os.environ.get("TL_API_KEY", ""), int(os.environ.get("TL_PLAN_ID", "0"))
name = os.environ.get("TL_BUILD") or os.environ.get("PIPELINE_ID", "local")
if not key or not plan:
    sys.exit("Falta TL_API_KEY o TL_PLAN_ID")
r = xmlrpc.client.ServerProxy(url).tl.createBuild(
    {"devKey": key, "testplanid": plan, "buildname": name, "buildnotes": "Creado por el pipeline"})
print("createBuild:", name, "->", r)
