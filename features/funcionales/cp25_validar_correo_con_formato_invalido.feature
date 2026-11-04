# language: es
Característica: CP-25 Validar correo con formato inválido
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-25
  Escenario: CP-25 Validar correo con formato inválido
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario con el correo "maria.correo.com"
    Y confirmo el pago
    Entonces veo el error del campo "correo"
    Y no se muestra la confirmación de compra
