# language: es
Característica: CP-30 Ver pantalla de confirmación
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-30
  Escenario: CP-30 Ver pantalla de confirmación
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces veo la pantalla de confirmación
    Y el pedido tiene número de orden y estado "Confirmado"
    Y el total pagado es 329.00
