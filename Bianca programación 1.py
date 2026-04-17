#Ejercicio 1, par o impar 

number= int(input("Introduce un número entero:"))
if number % 2 == 0:
    print(f"el número {number} es par")
else:
    print(f"el número {number} es impar")
    
#Ejercicio 2, Positivo,Negativo o Cero.

number= int(input("Introduce un número:"))
if number > 0:
    print("Es positivo")
elif number < 0:
    print("Es negativo")
else:
    print("Es neutro")
    
#Ejercicio 3, Verificación de la mayoría de edad.

edad = int(input("Introduce tu edad:"))
if edad >= 18:
    print("Eres mayor de edad,bienvenid@")
else: 
    print("Eres menor de edad,no tienes acceso")
    
#Ejercicio 4, Aprobado o Reprobado.

califi= float(input("Introduce tu calificación aquí (del 1 al 100):"))
if califi > 100 or califi < 0:
    print("Error,el número ingresado no está permitido.")
elif califi >= 60:
    print("Aprobado")
else:
    print("Reprobado")
    
#Ejercicio 5, El mayor de Dos números.

número1= float(input("Introduce el primer número para comparar."))
número2= float(input("Introduce el segundo número."))
if número1 > número2:
    print(f"El número mayor es {número1}")
elif número2 > número1:
    print(f"El número mayor es {número2}")
else:
    print("Son iguales.")
    
#Ejercicio 6, Descuentos.

compra = float(input("introduce el total a pagar de la compra:"))
if compra > 100:
    descuento = compra * 0.15
    total = compra - descuento
    print(f" ¡tienes descuento! el total a pagar es: ${total}")
else:
    print(f"no hay descuento,"
    f" el total a pagar es: ${compra}")
    
# ejercicio 7, Días de la semana.

dia = int(input("introduce el dia de la semana:"))
if dia == 1:
    print("lunes")
elif dia == 2:
    print("martes")
elif dia == 3:
    print("miercoles")
elif dia == 4:
    print("jueves")
elif dia == 5:  
    print("viernes")
elif dia == 6:
    print("sabado")
elif dia == 7:
    print("domingo")
else:
    print("error")
    
#Ejercicio 8, Año Bisiesto

año= int(input("Introduce un año:"))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else: 
    print(f"El año {año} no es bisiesto.")
    
    
    













