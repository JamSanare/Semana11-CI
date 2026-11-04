"""Configuración compartida por las pruebas Selenium (unittest), Behave y Playwright."""

import os
from pathlib import Path

# Raíz del proyecto (carpeta que contiene app/, pages/, tests/, features/...).
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# URL de la aplicación bajo prueba.
# - Con la variable de entorno BASE_URL (Docker, GitHub Actions, Jenkins) se usa esa URL,
#   por ejemplo: http://tiendademo/tienda_demo.html
# - Sin ella, se abre el archivo local app/tienda_demo.html (file://), como antes.
#   Path.as_uri() funciona igual en Windows, macOS y Linux.
BASE_URL = os.environ.get("BASE_URL") or (PROJECT_ROOT / "app" / "tienda_demo.html").as_uri()

# Carpeta donde se guardan capturas de pantalla de evidencia.
EVIDENCE_DIR = Path(os.environ.get("EVIDENCE_DIR") or PROJECT_ROOT / "evidencias")
