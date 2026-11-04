"""BasePage (Playwright): métodos comunes a todas las vistas de TiendaDemo.

Playwright espera automáticamente a que un elemento sea visible, estable y
reciba clics antes de pulsarlo, así que no se necesitan esperas explícitas
ni reintentos cuando el toast tapa momentáneamente un botón.
"""


class BasePage:
    TOAST = "#toast"

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    # Indica si existe al menos un elemento con ese selector (sin esperar).
    def exists(self, selector):
        return self.page.locator(selector).count() > 0

    # Indica si el elemento existe y es visible (sin esperar).
    def is_visible(self, selector):
        return self.page.locator(selector).first.is_visible()

    # Texto visible de un elemento o '' si no existe.
    def text_of(self, selector):
        loc = self.page.locator(selector)
        return loc.first.inner_text() if loc.count() else ""

    # Texto del toast; se usa textContent porque el toast entra con animación.
    def get_toast_text(self):
        return (self.page.locator(self.TOAST).text_content() or "").strip()

    def toast_is_visible(self):
        return "visible" in (self.page.locator(self.TOAST).get_attribute("class") or "")
