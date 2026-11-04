# language: es
Característica: CP-37 Confirmar pedido final
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-37
  Escenario: CP-37 Confirmar pedido final
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces puedo confirmar que mi pedido se realizó con su número de orden
