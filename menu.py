print ("Eliga una opcion")
print ("0.Comparacion de numeros.\n1. Suma\n2. Resta.\n3. Division.")
print ("4. Datos del usuario.\n 5. Multiplicacion dos digitos.")
print("6.Multiplicacionde de clase")
print ("7. Salir")
n=int (input("Ingrese la opcion: "))
if n==0:
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    if a==b:
        print(a," los numeros son iguales ",b)
    if a<b:
        print(a,"es menor que",b,"son diferentes")
    elif a>b:
        print (a," es mayor que ",b,"son diferentes")
if n==1:
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La suma de los dos numeros es",a+b)
if n==2:
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La resta de los dos numeros es",a-b)
if n==3:
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La division de los dos numeros es",a/b)
if n==4:
    name=input ("Dame tu nombre")
    apell=input ("Tu apellido")
    peso=float (input("Tu peso"))
    lista=[name,apell,peso]
    for lista in lista:
        print (lista)
if n==5:
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La multiplicacion de los dos numeros es",a*b)
if n==6:
    print("Multiplicacion de la tabla")
    m=int (input ("Elige la tabla de multiplicar que desees "))
    o=int (input ("El valor final del rango "))
    for u in range(1,o+1):
        print (u,"*",m,"=",u*m)
if n==7:
    print (" ")
