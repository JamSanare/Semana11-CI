# language: es
Característica: CP-21 Confirmar checkout con datos vacíos
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-21
  Escenario: CP-21 Confirmar checkout con datos vacíos
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando confirmo el pago sin completar los datos
    Entonces veo errores en todos los campos obligatorios
    Y no se muestra la confirmación de compra
