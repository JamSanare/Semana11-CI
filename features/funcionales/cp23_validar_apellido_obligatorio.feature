# language: es
Característica: CP-23 Validar apellido obligatorio
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  # DEF-01 (defecto conocido): la app no tiene campo "Apellido" y confirma la
  # compra con un nombre de una sola palabra. Este escenario FALLA hasta que se corrija.
  @funcional @defecto @CP-23
  Escenario: CP-23 Validar apellido obligatorio
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario dejando vacío el campo "apellido"
    Y confirmo el pago
    Entonces veo el error del campo "apellido"
    Y no se muestra la confirmación de compra
