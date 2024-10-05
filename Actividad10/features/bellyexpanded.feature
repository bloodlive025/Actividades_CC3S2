  # language: es

  Característica: Característica del Estómago Extendida

    Escenario: Comer diferentes cantidades de pepinos en varios tiempos
        Dado que he comido "30" pepinos
        Cuando espero "una hora y treinta minutos"
        Entonces mi estómago debería gruñir

    Escenario: Comer pepinos sin especificar cantidad exacta
        Dado que he comido "un monton de" pepinos
        Cuando espero "3 horas"
        Entonces mi estómago debería gruñir

    Escenario: Comer pepinos y esperar un tiempo exacto en minutos
        Dado que he comido "20" pepinos
        Cuando espero "120 minutos"
        Entonces mi estómago debería gruñir

    Escenario: Comer pepinos en palabras y tiempo en minutos
        Dado que he comido "veinticinco" pepinos
        Cuando espero "noventa minutos"
        Entonces mi estómago debería gruñir


    Escenario: Comer una cantidad no válida de pepinos
        Dado que he comido "1000" pepinos
        Cuando espero "2 horas"
        Entonces el sistema debe arrojar un error de cantidad no valida
        
    Escenario: Comer pepinos y esperar en segundos
        Dado que he comido "40" pepinos
        Cuando espero "5400 segundos"
        Entonces mi estómago debería gruñir

    Escenario: Comer una cantidad no válida de pepinos
      Dado que he comido "thirty-one" pepinos
      Cuando espero "one hours thirty minutes"
      Entonces mi estómago debería gruñir

    Escenario: Comer pepinos y esperar un tiempo aleatorio
        Dado que he comido "25" pepinos
        Cuando espero un tiempo aleatorio entre 1 y 3 horas
        Entonces mi estómago debería gruñir

    Escenario: Comer medio pepino y esperar
        Dado que he comido 0.5 pepinos
        Cuando espero "2 horas"
        Entonces mi estómago no debería gruñir
