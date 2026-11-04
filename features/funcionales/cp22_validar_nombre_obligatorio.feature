# language: es
Característica: CP-22 Validar nombre obligatorio
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-22
  Escenario: CP-22 Validar nombre obligatorio
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario dejando vacío el campo "nombre"
    Y confirmo el pago
    Entonces veo el error del campo "nombre"
    Y no se muestra la confirmación de compra
