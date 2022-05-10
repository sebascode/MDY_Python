def Menu():
    print("Bienvenido a la calculadora")
    print("""
    1. Sumar
    2. Restar
    3. Dividir
    4. Multiplicar
    5. Salir""")

def Sumar():
    num1 = input("Ingrese número 1")
    num2 = input("Ingrese número 2")
    return (int)(num1) + (int)(num2)

def Restar():
    num1 = input("Ingrese número 1")
    num2 = input("Ingrese número 2")
    return (int)(num1) - (int)(num2)

def Dividir():
    num1 = input("Ingrese número 1")
    num2 = input("Ingrese número 2")
    return (int)(num1) / (int)(num2)

def Multiplicar():
    num1 = input("Ingrese número 1")
    num2 = input("Ingrese número 2")
    return (int)(num1) * (int)(num2)

# Desplegar menu
opcion = 0
contador = 0
while(opcion != 5):
    
    contador = contador+1
    print("Contador: ",contador)

    Menu()
    # Preguntamos Input
    opcion = (int)(input("¿Qué opcion desea?"))
    if(opcion == 1):
        print(Sumar())
    elif(opcion == 2):
        print(Restar())
    elif(opcion == 3):
        print(Dividir())
    elif(opcion == 4):
        print(Multiplicar())
    else:
        print("Saliendooooo")
        exit