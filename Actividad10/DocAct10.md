<h1>BDD con Behave y Gherkin</h1>
Las historias de  usuario y criterios de aceptacion que se usaran inicialmente son los siguientes:


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


<h2>Usando el comando Behave</h2>

![](image.png)

![](image-1.png)


-Se puede observar que las 10 historias pasaran

<h2>Analizando el codigo</h2>

El primer script que analizaremos sera belly.py:

```shell
# src/belly.py
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos = pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado = tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False
    
    def cantidad_invalida(self):
        if self.pepinos_comidos > 50:
            return True
        return False

```

Definimos la clase belly, donde guardaremos los datos de la cantidad de pepinos comidos,  y el tiempo transcurrido, tambien añadiremos una funcion para verificar si el estomago esta gruñendo y una funcion para verificar si la cantidad es valida o no.

El siguiente script que analizaremos es belly.step:

```shell
from behave import given, when, then
from src.belly import Belly
import re

# Crear una instancia de Belly
belly = Belly()

#Funcion para verificar si lo ingresado es un numero

def isDigit(digit):
    if digit  is None or digit=='':
        return False    
    try:
        int(digit)
        return True
    except ValueError:
        return False


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    pattern=r'(\w*)\s*y*\s*(\w*)'
    match = re.search(pattern,palabra)
    numeros = {
        "uno" or "una" or "1": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once":11 , "doce":12,
"veinte": 20, "veintuno":21, "veintidos":22,
"veintitres":23, "veinticuatro":24, "veinticinco":25,"veintiseis":26,
"veintisiete":27,"veintioscho":28,"veintinueve":29,
 "treinta": 30, "cuarenta": 40, "cincuenta": 50,
"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
    }
    num1= numeros.get(match.group(1),0)
    num2=numeros.get(match.group(2),0)
    res=num1+num2
    return res  # Retornar 0 si la palabra no está en el diccionario

```

Esta primera parte del codigo empieza importando las clases given,when,then del modulo behave, tambien importaremos la clase Belly y la libreria re

Creamos una instancia de la clase Belly, llamada belly, y definimos las siguientes funciones que se utilizaran mas adelante:

-isDigit(digit): Esta funcion devolvera True si el valor pasado es del tipo int, de lo contrario retornara False, adicionalmente retornara un False si la cadena pasada esta vacia.

-convertir_palabra_a_numero(palabra): Esta funcion convertira el string palabra a un numero de tipo int. Se usara el patron <h3>(\w*)\s*y*\s*(\w*) </h3> 

para poder capturar los digitos cuando la palabra es compuesta como por ejemplo "treinta y cinco". Esta funcion solo convertira las palabras de los numeros del 1 al 99.


```shell
@given('que he comido "{cantidad}" pepinos')
def step_given_comido_variable(context,cantidad):
    pattern = re.compile(r'(?:al menos\s)?(?:menos\sde\s)?(?:mas\sde\s)?(?:un\smonton\sde)?(?:(\w*)?)?')
    match = pattern.match(cantidad.lower())
    if 'un monton de' in cantidad:
        belly.comer(11)
        return 0
    print(match.group(1))
    if match.group(0)!='':
        if isDigit(match.group(1)):
            number_pepinos=match.group(1)
            if "mas de" in cantidad:
                belly.comer(int(number_pepinos)+1)
            elif "menos de" in cantidad:
                belly.comer(int(number_pepinos)-1)
            else:
                belly.comer(int(number_pepinos))  
        else:
            number_pepinos=convertir_palabra_a_numero(match.group(1))
            if "mas de" in cantidad:
                belly.comer(int(number_pepinos)+1)
            elif "menos de" in cantidad:
                belly.comer(int(number_pepinos)-1)
            else:
                belly.comer(number_pepinos)        
    else:
        raise ValueError(f"No se pudo interpretar la cantidad de pepino: {cantidad}")

```

La siguiente parte del codigo de belly_steps.py que analizaremos sera la funcion step_given_comido_variable que tiene como decorador @given.

