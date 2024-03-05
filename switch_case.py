## Crea un programa que solicite al usuario ingresar un número del 1 al 7, representando cadadía de la semana (1 para lunes, 2 para martes, y así sucesivamente). Utiliza esta entrada para calcular y mostrar el nombre correspondiente al día de la semana.Pasos a seguir:1. Entrada de Datos:
##• Solicita al usuario ingresar un número del 1 al 7.
##2. Cálculo del Día:
##• Utiliza una estructura de control switch para determinar el nombre del día de la
##semana basándote en el número ingresado por el usuario. Asigna el nombre del día
##correspondiente a una variable.
##3. Salida de Resultados:
##• Imprime en la pantalla el nombre del día de la semana calculado

##El ejercicio deberá ser realizado con if y elif ya que python no cuenta con switch.

numero = int(input("Ingrese un numero del 1 al 7: "))

if numero == 1:
    print("Su dia es: Lunes") 
elif numero == 2:
    print("Su dia es: Martes")
elif numero == 3:
    print("Su dia es: Miercoles")
elif numero == 4:
    print("Su dia es: Jueves")
elif numero == 5:
    print("Su dia es: viernes")
elif numero == 6:
    print("Su dia es: Sabado")
elif numero == 7:
    print("Su dia es: Domingo")
elif numero <= 0:
    print("Solo se admiten numeros del 1 al 7.")
elif numero >= 8:
    print("Solo se admiten numeros del 1 al 7 como maximo.")
