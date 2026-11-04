# language: es
Característica: CP-28 Confirmar compra con datos válidos
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-28
  Escenario: CP-28 Confirmar compra con datos válidos
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces veo la pantalla de confirmación
