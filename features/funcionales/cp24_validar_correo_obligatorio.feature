# language: es
Característica: CP-24 Validar correo obligatorio
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-24
  Escenario: CP-24 Validar correo obligatorio
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario dejando vacío el campo "correo"
    Y confirmo el pago
    Entonces veo el error del campo "correo"
    Y no se muestra la confirmación de compra
