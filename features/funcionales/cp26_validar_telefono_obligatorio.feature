# language: es
Característica: CP-26 Validar teléfono obligatorio
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-26
  Escenario: CP-26 Validar teléfono obligatorio
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario dejando vacío el campo "teléfono"
    Y confirmo el pago
    Entonces veo el error del campo "teléfono"
    Y no se muestra la confirmación de compra
