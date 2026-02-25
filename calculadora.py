import math

def suma(a,b):
    return a + b 

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b 

def division(a,b):
    if b == 0:
        return"Error: no se puede dividir entre cero"
    return a / b 

def potencia(a,b):
    return a ** b 

def raiz(a,b):
    if a < 0:
        return "Error: no existe raiz real de numero negativo"
    return math.sqrt(a)

def porcentaje(a,b):
    return (a * b) / 100

def modulo(a,b):
    return a % b 

def promedio(lista):
    return sum(lista) / len(lista)    

# MENU
while True:
    print("\n--- CALCULADORA ---")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potencia")
    print("6. raiz")
    print("7. porcentaje")
    print("8. modulo")
    print("9. promedio")
    print("0. salir")

    opcion = input("elige una opcion: ")

    if opcion == "0": 
        print("programa finalizado")
        break

    elif opcion == "1":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", suma(a,b))

    elif opcion == "2":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", resta(a,b))

    elif opcion == "3":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", multiplicacion(a,b))    

    elif opcion == "4":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", division(a,b)) 

    elif opcion == "5":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", potencia(a,b))  
    
    elif opcion == "6":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", raiz(a,b))    

    elif opcion == "7":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", porcentaje(a,b))    
    
    elif opcion == "8":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", modulo(a,b))    

    elif opcion == "9":
        a = float(input("primer numero"))
        b = float(input("segundo numero:"))
        print("resultado:", promedio(a,b))    

    elif opcion == "9":

        datos = input("Ingresa números separados por coma: ")
        lista = [float(x) for x in datos.split(",")]
        print("Resultado:", promedio(lista))


    else:
        print("Opción inválida")
























