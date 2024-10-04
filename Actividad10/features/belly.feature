  # language: es

  Característica: Comportamiento del estómago

    Escenario: Comer más de 10 pepinos y esperar al menos 2 horas
      Dado que he comido "mas de 10" pepinos
      Cuando espero "al menos 2 horas"
      Entonces mi estómago debería gruñir


    Escenario: Comer menos de 10 pepinos y esperar 2 horas
      Dado que he comido "menos de 10" pepinos
      Cuando espero "2 horas"
      Entonces mi estómago no debería gruñir


    Escenario: Comer más de 10 pepinos y esperar menos de 1 hora
      Dado que he comido "mas de 10" pepinos
      Cuando espero "menos de 1 hora"
      Entonces mi estómago no debería gruñir

    Escenario: Comer más de 10 pepinos y esperar al menos 90 minutos
      Dado que he comido "mas de 10" pepinos
      Cuando espero "al menos 90 minutos"
      Entonces mi estómago debería gruñir


    Escenario: Comer más de 10 pepinos y esperar "dos horas y treinta minutos"
      Dado que he comido "mas de 10" pepinos
      Cuando espero "dos horas y treinta minutos"
      Entonces mi estómago debería gruñir

    Escenario: Comer más de 10 pepinos y esperar "una hora y treinta minutos"
      Dado que he comido "mas de 10" pepinos
      Cuando espero "una hora y treinta minutos"
      Entonces mi estómago debería gruñir
  
    Escenario: Comer "un montón" de pepinos y esperar 3 horas
      Dado que he comido "un monton de" pepinos
      Cuando espero "3 horas"
      Entonces mi estómago debería gruñir

    Escenario: Comer más de 10 pepinos y esperar 120 minutos
      Dado que he comido "mas de 10" pepinos
      Cuando espero "120 minutos"
      Entonces mi estómago debería gruñir

    Escenario: Comer "veinticinco pepinos" y esperar 90 minutos
      Dado que he comido "veinticinco" pepinos
      Cuando espero "90 minutos"
      Entonces mi estómago debería gruñir

    Escenario: Comer una cantidad no válida de pepinos
      Dado que he comido "100" pepinos
      Cuando espero "2 horas"
      Entonces el sistema debe arrojar un error de cantidad no valida






    