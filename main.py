from sumar import sumar
from resta import restar
from multiplicacion import multiplicar 
from dividir import dividir
from suma_avanzada import suma_avanzada


print("Hola bienvenido a tu calculadora de confianza :D")

operacion = ''

while operacion != 'salir':

    operacion = input("Elije la opcion que se adapte a tus necesidades: \n"
    "-----'suma', \n"
    "-----'resta', \n"
    "-----'multiplicacion', \n"
    "-----'division', \n"
    "-----'suma avanzada', \n"
    "'salir:'"
    "")

    if operacion == 'suma':
        x = float(input("Ingresa el primer numero: "))
        y = float(input("Ingresa el segundo número: "))
        resultado = sumar(x, y)
        print("El resultado es:", resultado)

    if operacion == 'resta':
        x = float(input("Ingresa el primer numero: "))
        y = float(input("Ingresa el segundo número: "))
        resultado = restar(x, y)
        print("El resultado es:", resultado)

    if operacion == 'multiplicacion':
        x = float(input("Ingresa el primer numero: "))
        y = float(input("Ingresa el segundo número: "))
        resultado = multiplicar(x, y)
        print("El resultado es:", resultado)

    if operacion == 'division':
        x = float(input("Ingresa el primer numero: "))
        y = float(input("Ingresa el segundo número: "))
        resultado = dividir(x, y)
        print("El resultado es:", resultado)

    if operacion == 'suma avanzada':
        numeros = input("Digita los numeros que deseas sumar separdos por una ',':  ")

        lista_n = numeros.split(",")

        lista_numeros = []
        for n in lista_n:
            numero = float(n)
            lista_numeros.append(numero)
        

        resultado = suma_avanzada(lista_numeros)
        print("El resultado de tu suma es:", resultado)

