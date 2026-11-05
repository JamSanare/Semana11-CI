"""Genera testlink-import.xml. El orden importa: TestLink numera AN-1, AN-2... en el orden de importación.
CP-01..CP-41 van primero (AN-1..AN-41), luego rd (42-51), es (52-61), se (62-71)."""
import glob, os, re
from xml.sax.saxutils import escape, quoteattr

def titulo(path):
    base = os.path.basename(path).rsplit(".", 1)[0]
    m = re.match(r"^([a-z]{2})[-_]?(\d+)[-_](.*)$", base)
    pre, n, resto = m.groups()
    txt = resto.replace("-", " ").replace("_", " ").capitalize()
    return f"{pre.upper()}-{n} {txt}", base

def caso(path, herramienta):
    nombre, base = titulo(path)
    return (f"    <testcase name={quoteattr(nombre)}>\n"
            f"      <summary>{escape('Automatizado con ' + herramienta + ' (' + base + ')')}</summary>\n"
            f"      <preconditions>Entorno levantado con Docker Compose</preconditions>\n"
            f"      <execution_type>2</execution_type>\n"
            f"      <steps><step><step_number>1</step_number>"
            f"<actions>{escape('Ejecutar ' + base)}</actions>"
            f"<expectedresults>Resultado esperado según el escenario</expectedresults>"
            f"<execution_type>2</execution_type></step></steps>\n"
            f"    </testcase>\n")

def suite(nombre, archivos, herramienta):
    return f"  <testsuite name={quoteattr(nombre)}>\n" + "".join(caso(a, herramienta) for a in archivos) + "  </testsuite>\n"

func = sorted(glob.glob("features/funcionales/*.feature")) + sorted(glob.glob("features/uat/*.feature"))
out = '<?xml version="1.0" encoding="UTF-8"?>\n<testsuite name="Semana11">\n'
out += suite("Funcionales y UAT (Selenium y Playwright)", func, "Selenium / Playwright")
out += suite("Rendimiento k6", sorted(glob.glob("aulavirtual/pruebas/k6/rendimiento/*.js")), "Grafana k6")
out += suite("Estres k6", sorted(glob.glob("aulavirtual/pruebas/k6/estres/*.js")), "Grafana k6")
out += suite("Seguridad k6", sorted(glob.glob("aulavirtual/pruebas/k6/seguridad/*.js")), "Grafana k6")
out += "</testsuite>\n"
open("testlink-import.xml", "w", encoding="utf-8").write(out)
print("Casos:", out.count("<testcase "), "(esperado 71)")
