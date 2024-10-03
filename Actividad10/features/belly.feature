  # language: es

  Característica: Comportamiento del estómago

    Escenario: Comer 25 pepinos y esperar 2 horas
      Dado que he comido "12" pepinos
      Cuando espero "1 hora y 29 minutos"
      Entonces mi estómago debería gruñir

    Escenario: Comer doce pepinos y esperar dos horas
      Dado que he comido "ocho" pepinos
      Cuando espero "1 hora"
      Entonces mi estómago no debería gruñir

    Escenario: Comer 8 pepinos y esperar una horas
      Dado que he comido "once" pepinos
      Cuando espero "1 hora"
      Entonces mi estómago no debería gruñir