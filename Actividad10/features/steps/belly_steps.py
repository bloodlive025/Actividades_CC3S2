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
    numeros = {
        "uno" or "una" or "1": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once":11 , "doce":12,
"veinte": 20, "veintuno":21, "veintidos":22,
"veintitres":23, "veinticuatro":24, "veinticinco":25,"veintiseis":26,
"veintisiete":27,"veintioscho":28,"veintinueve":29,
 "treinta": 30, "cuarenta": 40, "cincuenta": 50,
"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
    }
    return numeros.get(palabra, 0)  # Retornar 0 si la palabra no está en el diccionario


#Diccionario extendido para numeros
numeros_extendido = {
    "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
"veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
}

@given('que he comido "{cantidad}" pepinos')
def step_given_comido_variable(context,cantidad):
    #Manejar cantidades no numericas
    if isDigit(cantidad):
        belly.comer(int(cantidad))
    else:
        pattern= re.compile(r'(?:([A-z,a-z]+|\d+))?(?:\s?)?(?:([A-z,a-z]+|\d+))?')
        match=pattern.match(cantidad.lower())

        if match:
            decenas=match.group(1) if match.group(1) else "0"
            unidades=match.group(2) if match.group(2) else "0"
            decenas=convertir_palabra_a_numero(decenas)
            unidades=convertir_palabra_a_numero(unidades)
            numero=decenas+unidades
            belly.comer(numero)
        else:
            raise ValueError(f"No se pudo interpretar la descripcion de los pepinos: {cantidad}")
    



# Cuando espero "{time_description}"
@when('espero "{time_description}"')
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(r'(?:([A-z,a-z]+|\d+)\shoras?)?(?:\s*y?\s*)?(?:([A-z,a-z]+|\d+)\sminutos?)?')
    match = pattern.match(time_description.lower())
    
    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if match:
        if isDigit(match.group(1)) or isDigit(match.group(2)): 
            horas=int(match.group(1)) if isDigit(match.group(1)) else 0
            minutos=int(match.group(2))/60 if isDigit(match.group(2)) else 0
            belly.esperar(horas + minutos)
        else:
            hours_word = match.group(1) if match.group(1) else "0"
            minutes_word = match.group(2) if match.group(2) else "0"
            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            total_time_in_hours = hours + (minutes / 60)
            belly.esperar(total_time_in_hours)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")






# Entonces mi estómago debería gruñir
@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

# Entonces mi estómago no debería gruñir
@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."








