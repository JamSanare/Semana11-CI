#!/usr/bin/env bash
# Ejecuta la suite Playwright (41 casos) y deja el informe JUnit en reports/playwright/.
set -u
cd "$(dirname "$0")/.."

mkdir -p reports/playwright

pytest tests/playwright --junitxml=reports/playwright/results.xml
