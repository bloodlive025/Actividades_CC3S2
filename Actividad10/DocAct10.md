<h1>BDD con Behave y Gherkin</h1>
Las historias de  usuario y criterios de aceptacion que se usaran inicialmente son los siguientes:\\

<h2>Historia de usuario 1: Comer muchos pepinos y esperar el tiempo suficiente</h2>

- **Como** una persona que ha comido una cantidad considerable de pepinos,  
- **Quiero** que mi estómago comience a gruñir después de esperar al menos 2 horas,  
- **Para** saber si he comido lo suficiente para sentirme lleno y detectar cuando he comido en exceso.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero al menos 2 horas,  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 2: Comer pocos pepinos y no gruñir</h2>

- **Como** una persona que ha comido una pequeña cantidad de pepinos,  
- **Quiero** que mi estómago no gruña si no he comido lo suficiente,  
- **Para** saber que aún no he comido lo necesario para sentirme lleno.

**Criterios de aceptación**:  
- **Dado** que he comido menos de 10 pepinos,  
- **Cuando** espero 2 horas,  
- **Entonces** mi estómago no debería gruñir.

<h2>Historia de usuario 3: Comer muchos pepinos y esperar menos de una hora</h2>

- **Como** una persona que ha comido muchos pepinos,  
- **Quiero** que mi estómago no gruña si no he esperado el tiempo suficiente,  
- **Para** saber que todavía no es el momento adecuado para sentirme lleno.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero menos de 1 hora,  
- **Entonces** mi estómago no debería gruñir.

<h2>Historia de usuario 4: Comer pepinos y esperar en minutos</h2>

- **Como** una persona que ha comido una cantidad moderada de pepinos,  
- **Quiero** que mi estómago gruña si he esperado el tiempo equivalente a al menos 1.5 horas, aunque lo exprese en minutos,  
- **Para** tener la flexibilidad de medir el tiempo de espera en minutos.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero al menos 90 minutos,  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 5: Comer pepinos y esperar en diferentes formatos de tiempo</h2>

- **Como** una persona que ha comido una cantidad moderada de pepinos,  
- **Quiero** que mi estómago gruña si he esperado el tiempo suficiente, incluso cuando el tiempo de espera se exprese en formatos complejos como "dos horas y treinta minutos",  
- **Para** tener la flexibilidad de usar diferentes formatos de tiempo.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero "dos horas y treinta minutos",  
- **Entonces** mi estómago debería gruñir.

<h2>Nuevas historias de usuario (Extensiones)</h2>

<h2>Historia de usuario 6: Comer diferentes cantidades de pepinos y esperar en varios tiempos</h2>

- **Como** una persona que ha comido una cantidad moderada de pepinos,  
- **Quiero** que mi estómago gruña si he esperado un tiempo razonable (por ejemplo, "una hora y treinta minutos"),  
- **Para** que el sistema pueda manejar distintos tiempos de espera expresados en diferentes combinaciones.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero "una hora y treinta minutos",  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 7: Comer pepinos sin especificar una cantidad exacta</h2>

- **Como** una persona que ha comido pepinos, pero sin especificar una cantidad exacta (por ejemplo, "un montón"),  
- **Quiero** que mi estómago gruña si he esperado un tiempo razonable,  
- **Para** permitir más flexibilidad en la entrada de datos de cuántos pepinos he comido.

**Criterios de aceptación**:  
- **Dado** que he comido "un montón" de pepinos,  
- **Cuando** espero 3 horas,  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 8: Comer pepinos y esperar un tiempo exacto en minutos</h2>

- **Como** una persona que ha comido una cantidad moderada de pepinos,  
- **Quiero** poder expresar el tiempo de espera en minutos exactos y que el sistema lo acepte (por ejemplo, 120 minutos),  
- **Para** tener más control sobre la forma en la que expreso el tiempo de espera.

**Criterios de aceptación**:  
- **Dado** que he comido más de 10 pepinos,  
- **Cuando** espero 120 minutos,  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 9: Comer pepinos expresados en palabras y esperar el tiempo en minutos</h2>

- **Como** una persona que ha comido una cantidad moderada de pepinos expresada en palabras (por ejemplo, "veinticinco pepinos"),  
- **Quiero** que mi estómago gruña si he esperado un tiempo expresado en minutos,  
- **Para** combinar la flexibilidad de entrada tanto en palabras como en tiempos expresados numéricamente.

**Criterios de aceptación**:  
- **Dado** que he comido "veinticinco pepinos",  
- **Cuando** espero 90 minutos,  
- **Entonces** mi estómago debería gruñir.

<h2>Historia de usuario 10: Comer una cantidad no válida de pepinos</h2>

- **Como** una persona que ha ingresado una cantidad no válida de pepinos (por ejemplo, "mil pepinos"),  
- **Quiero** que el sistema me advierta si he ingresado una cantidad excesiva,  
- **Para** evitar errores en el sistema debido a entradas no realistas.

**Criterios de aceptación**:  
- **Dado** que he ingresado una cantidad no válida de pepinos,  
- **Cuando** espero cualquier cantidad de tiempo,  
- **Entonces** el sistema debería arrojar un error de cantidad no válida.
