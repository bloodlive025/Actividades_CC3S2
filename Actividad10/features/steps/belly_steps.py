from behave import given, when, then
from src.belly import Belly
import re,random

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
    pattern=r'(.*)\s*y*\s*(.*)'
    match = re.search(pattern,palabra)
    numeros = {
        "uno": 1, "una":1 ,"dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once":11 , "doce":12,
"trece":13,"catorce":14,"quince":15,"dieciseis":16,"diecisiete":17,"dieciocho":18,"diecinueve":19,
"veinte": 20, "veintuno":21, "veintidos":22,
"veintitres":23, "veinticuatro":24, "veinticinco":25,"veintiseis":26,
"veintisiete":27,"veintioscho":28,"veintinueve":29, 
"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,
"eighteen":18,"nineteen":19,"twenty":20,"twenty-one":21,"twenty-two":22,"twenty-three":23,"twenty-four":24,
"twenty-five":25,"twenty-six":26,"twenty-seven":27,"twenty-eight":28,"twenty-nine":29,"thirty":30,"thirty-one":31,
"thirty-two": 32, "thirty-three": 33, "thirty-four": 34, "thirty-five": 35, "thirty-six": 36, 
"thirty-seven": 37, "thirty-eight": 38, "thirty-nine": 39, "forty": 40, "forty-one": 41, 
"forty-two": 42, "forty-three": 43, "forty-four": 44, "forty-five": 45, "forty-six": 46, 
"forty-seven": 47, "forty-eight": 48, "forty-nine": 49, "fifty": 50

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

@given('que he comido {cantidad:f} pepinos')
def step_given_eaten_fractional_cukes(context, cantidad):
    belly.comer(cantidad)

        



# Cuando espero "{time_description}"
@when('espero "{time_description}"')
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(r'(?:al\smenos\s|menos\sde\s|mas\sde\s?)?(?:(.*)\s(?:horas?|hours?))?(?:\s*y?\s*)?(?:(.+)\s(?:minutos?|minutes?))?(?:\s*y?\s*)?(?:(.+)\s(?:segundos?|seconds?))?')
    match = pattern.match(time_description.lower())
    print(match.group(2))
    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if isDigit(match.group(1)) or isDigit(match.group(2)) or isDigit(match.group(3)): 
        hours=int(match.group(1)) if isDigit(match.group(1)) else 0
        minutes=int(match.group(2))/60 if isDigit(match.group(2)) else 0
        seconds=int(match.group(3))/3600 if isDigit(match.group(3)) else 0
        if "mas de" in time_description:
            belly.esperar(hours + minutes + seconds +0.017)
        elif "menos de" in time_description:
            belly.esperar(hours + minutes + seconds-0.017)
        else: 
            belly.esperar(hours+minutes+seconds)
    else:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        seconds_word=match.group(3) if match.group(3) else "0"
        print(minutes_word)
        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds=convertir_palabra_a_numero(seconds_word)
        total_time_in_hours = hours + (minutes/60) + (seconds/3600)
        print(hours,minutes,seconds)
        print(total_time_in_hours)
        if total_time_in_hours ==0:
            raise ValueError(f"Nose pudo interpretar la cantidad de pepinos:{match.group(0)}")
        if "mas de" in time_description:
            belly.esperar(total_time_in_hours+0.017)
        elif "menos de" in time_description:
            belly.esperar(total_time_in_hours-0.017)
        else: 
            belly.esperar(total_time_in_hours)

#Tiempo Aleatorio
@when('espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas')
def step_when_wait_random_time(context, min_time, max_time):
    tiempo_aleatorio = random.uniform(min_time, max_time)
    print(f"Esperando un tiempo aleatorio de {tiempo_aleatorio:.2f} horas.")
    belly.esperar(tiempo_aleatorio)




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








