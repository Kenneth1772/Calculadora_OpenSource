from sumar import sumar

def suma_avanzada(lista_numeros):
    total = 0
    for n in lista_numeros:
        total = sumar(total, n)
    return total
        
'''numeros = input("Digita los numeros que deseas sumar separdos por una ',':  ")

lista_n = numeros.split(",")

lista_numeros = []
for n in lista_n:
    numero = float(n)
    lista_numeros.append(numero)
    

resultado = suma_avanzada(lista_numeros)
print("El resultado de tu suma es:", resultado)
'''
        