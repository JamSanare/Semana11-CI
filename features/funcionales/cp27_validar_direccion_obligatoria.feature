# language: es
Característica: CP-27 Validar dirección obligatoria
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-27
  Escenario: CP-27 Validar dirección obligatoria
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario dejando vacío el campo "dirección"
    Y confirmo el pago
    Entonces veo el error del campo "dirección"
    Y no se muestra la confirmación de compra
