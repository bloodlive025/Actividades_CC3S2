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

    }

    
    numeros2 = {
        "uno" or "una" or "1": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9
    }

    numeros3 = {
 "treinta": 30, "cuarenta": 40, "cincuenta": 50,
"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
    }
    
    num1= numeros.get(match.group(1),0)
    num2=numeros2.get(match.group(2),0)
    num3=numeros3.get(match.group(1),0)
    if num1==0 and num3==0:
        return 0
    elif num3==0 and num2==0:
        return num1
    elif num3!=0 and num2!=0:
        res=num3+num2
        return res
    elif num3!=0 and match.group(2)=='':
        return num3
    else:
        return 0



#Diccionario extendido para numeros
numeros_extendido = {
    "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
"veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
}

@given('que he comido "{cantidad}" pepinos')
def step_given_comido_variable(context,cantidad):
    if 'un monton de' == cantidad:
        belly.comer(11)
        return 0
    pattern = re.compile(r'(?:al\smenos\s|menos\sde\s|mas\sde\s?)?(\w*\s?y?\s?\w*)?')
    match = pattern.match(cantidad.lower())
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
        if int(number_pepinos)==0:
            raise ValueError(f"Nose pudo interpretar la cantidad de pepinos:{match.group(0)}")
        if "mas de" in cantidad:
            belly.comer(int(number_pepinos)+1)
        elif "menos de" in cantidad:
            belly.comer(int(number_pepinos)-1)
        else:
            belly.comer(int(number_pepinos))        



        



# Cuando espero "{time_description}"
@when('espero "{time_description}"')
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(r'(?:al\smenos\s|menos\sde\s|mas\sde\s?)?(?:(.*)\shoras?)?(?:\s*y?\s*)?(?:(.+)\sminutos?)?')
    match = pattern.match(time_description.lower())
    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if isDigit(match.group(1)) or isDigit(match.group(2)): 
        hours=int(match.group(1)) if isDigit(match.group(1)) else 0
        minutes=int(match.group(2))/60 if isDigit(match.group(2)) else 0
        if "mas de" in time_description:
            belly.esperar(hours + minutes +0.017)
        elif "menos de" in time_description:
            belly.esperar(hours + minutes-0.017)
        else: 
            belly.esperar(hours+minutes)
    else:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        total_time_in_hours = hours + (minutes / 60)
        if total_time_in_hours ==0:
            raise ValueError(f"Nose pudo interpretar la cantidad de pepinos:{match.group(0)}")
        if "mas de" in time_description:
            belly.esperar(total_time_in_hours+0.017)
        elif "menos de" in time_description:
            belly.esperar(total_time_in_hours-0.017)
        else: 
            belly.esperar(hours+minutes)


    


# Entonces mi estómago debería gruñir
@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

# Entonces mi estómago no debería gruñir
@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('el sistema debe arrojar un error de cantidad no valida')
def cantidad_no_valida(context):
    assert belly.cantidad_invalida(), "Cantidad invalida de pepinos"








