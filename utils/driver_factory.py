"""
DriverFactory: crea y configura instancias del navegador para los tests.

Centraliza la configuración del driver Chrome para que los archivos de test
mantengan un único punto de creación del navegador.

Variables de entorno opcionales (útiles en CI o contenedores):
  CHROME_BINARY      ruta al ejecutable de Chrome/Chromium a usar.
  CHROMEDRIVER_PATH  ruta a un chromedriver concreto (si no, Selenium Manager).
  CHROME_NO_SANDBOX  "1" para añadir --no-sandbox (necesario al correr como root).
"""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class DriverFactory:
    # Crea un driver Chrome configurado para pruebas.
    #
    # El modo headless permite ejecutar los tests sin abrir una ventana
    # visible del navegador, lo cual es útil para entornos de CI o ejecución rápida.
    @staticmethod
    def create_chrome(headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        # Tamaño fijo: el diseño de la tienda es responsive y los
        # localizadores deben ver siempre la misma disposición.
        options.add_argument('--window-size=1366,900')

        if os.environ.get('CHROME_BINARY'):
            options.binary_location = os.environ['CHROME_BINARY']
        if os.environ.get('CHROME_NO_SANDBOX') == '1':
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

        driver_path = os.environ.get('CHROMEDRIVER_PATH')
        service = Service(driver_path) if driver_path else Service()
        driver = webdriver.Chrome(options=options, service=service)
        return driver
