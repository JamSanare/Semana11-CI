#!/usr/bin/env bash
# Ejecuta las suites Selenium y deja informes JUnit en reports/.
# Corre ambas suites aunque una falle; el código de salida es != 0 si alguna falló.
set -u
cd "$(dirname "$0")/.."

mkdir -p reports/selenium-unittest reports/selenium-behave evidencias

status=0

echo "=== Selenium · unittest (CP-01..CP-31) ==="
python -m xmlrunner discover -s tests -o reports/selenium-unittest || status=1

echo "=== Selenium · Behave (CP-01..CP-41) ==="
behave features --junit --junit-directory reports/selenium-behave || status=1

exit $status
