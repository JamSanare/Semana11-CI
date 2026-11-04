"""
BasePage: clase base del Page Object Model.

Este módulo contiene los métodos comunes que se utilizan en todas
las páginas de la aplicación TiendaDemo.

El patrón Page Object Model separa la lógica de interacción con la UI
de la lógica de los tests, lo cual mejora la mantenibilidad.
"""

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TOAST = (By.ID, "toast")

    # Inicializa el Page Object con el driver de Selenium y una espera explícita.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Abre una URL en el navegador conectado al driver.
    def open(self, url):
        self.driver.get(url)

    # Busca un elemento usando un localizador y espera a que esté presente.
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Indica si existe al menos un elemento con ese localizador (sin esperar).
    def exists(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    # Indica si el elemento existe Y es visible para el usuario (sin esperar).
    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return bool(elements) and elements[0].is_displayed()

    # Devuelve el texto de un elemento o '' si no existe.
    def text_of(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements[0].text if elements else ""

    # Hace clic en un elemento ya localizado. El toast flotante puede tapar
    # brevemente algunos botones: se espera a que se retire y se reintenta.
    def click_element(self, element):
        def _try_click(_driver):
            try:
                element.click()
                return True
            except ElementClickInterceptedException:
                return False
        self.wait.until(_try_click)
        return element

    # Hace clic en un elemento encontrado por el localizador.
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return self.click_element(element)

    # Llena un campo de texto: limpia primero y escribe el valor.
    def fill(self, locator, text):
        element = self.find(locator)
        element.clear()
        if text:
            element.send_keys(text)
        return element

    # Texto del toast (mensaje temporal) y si está visible en este momento.
    # Se lee textContent: .text devuelve '' mientras el toast aún se desliza
    # hacia la pantalla (animación CSS de 0,3 s), lo que daría falsos negativos.
    def get_toast_text(self):
        return (self.find(self.TOAST).get_attribute("textContent") or "").strip()

    def toast_is_visible(self):
        return "visible" in (self.find(self.TOAST).get_attribute("class") or "")
