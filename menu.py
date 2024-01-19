######################################################################
#Elaborado por: Emmanuel Naranjo Blanco y Jose Fabio Navarro Naranjo #
#Fecha de Creación: 13/03/2019 5:00pm                                #
#Fecha de última Modificación: 14/03/2019 10:00pm                    #
#Versión: 3.7.2                                                      #
######################################################################

#importanción de librerías

from funciones import*
""""funciones" es el archivo que contiene las funciones principales
a ser llamadas desde este archivo"""

#Definición de funciones
#Permiten el ingreso y salida de datos
def opcionBisiesto():#1
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Booleano que indica si el año es bisiesto o no
    """
    print ("\n------------------------\n")
    print ("Prueba del año bisiesto\n")
    annio = int(input("Ingrese un año positivo: "))
    print (esBisiesto(annio))
    
def opcionMasCercanos():#2
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Indicar el número más cercano a 0
    """
    print ("\n------------------------\n")
    print ("Prueba de la recta numérica\n")
    n1 = int(input("Ingrese n1 : "))
    n2 = int(input("Ingrese n2 : "))
    n3 = int(input("Ingrese n3 : "))
    n4 = int(input("Ingrese n4 : "))
    print (masCercanos(n1, n2, n3, n4))
    
def opcionAumentoTar():#3
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer el aumento de la tarifa del bus
    """
    print ("\n------------------------\n")
    print ("Prueba del aumento de la tarifa de buses\n")
    actual=int(input("Indique el monto actual (ej:120): "))
    porcentaje=int(input("Indique el porcentaje de aumento (ej:15): "))
    print("Subirá a: ",calcularTarifaAux(actual,porcentaje),"colones.")

def opcionImc():#4
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer el índice de masa corporal
    """
    print ("\n------------------------\n")
    print ("Prueba del Índice de Masa Corporal\n")
    peso=float(input("Indique su peso en kilogramos(ej:70): "))
    estatura=float(input("Indique su estatura en metros(ej:1.75): "))
    print("Usted tiene: ",calcularImcAux(peso,estatura))

def opcionTablaMult():#5
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Conocer la tabla de multiplicar del número dado
    """
    print ("\n------------------------\n")
    print ("Tabla de Multiplicar\n")
    num=int(input("Digite un número(ej:2): "))
    print(calcularTablaMulti(num))

    
def opcionRangoMult():#6
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer el rango de las tablas de multiplicar
    """
    print ("\n------------------------\n")
    print ("Prueba del rango de tablas de multiplicar\n")
    num1=int(input('coloque un numero entero: '))
    num2=int(input('coloque otro numero entero: '))
    print(aplicarRangoAux(num1,num2))
    
def opcionSumatoria():#7
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer la suma acumulada dado un numero entero positivo
    """
    print ("\n------------------------\n")
    print ("Prueba la sumatoria dado un numero\n")
    num=int(input('coloque un numero entero: '))
    print(determinarSumaAux(num))
    
def opcionTipoTri():#8
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer el tipo de triangulo segun los angulos dados
    """
    print ("\n------------------------\n")
    print ("Prueba del tipo de triangulo segun sus angulos\n")
    ang1=float(input('coloque el primer angulo (ej:45): '))
    ang2=float(input('coloque el segundo angulo (ej:45): '))
    ang3=float(input('coloque el tercer angulo (ej:90): '))
    print(saberTrianguloAux(ang1,ang2,ang3))

def opcionMultiCorrect():#9
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer si el resultado colocado fue correcto o no
    """
    print ("\n------------------------\n")
    print ("Prueba de multiplicación\n")
    fact1=float(input('Coloque el primer factor (ej:4): '))
    fact2=float(input('Coloque el segundo factor (ej:6): '))
    result=float(input('Coloque el resultado de la multiplicación de los factores(ej:24): '))
    print(calcularMultiCorrect(fact1,fact2,result))
    
def opcionEstadoAlum():#10
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: conocer el estado del alumno 
    """
    print ("\n------------------------\n")
    print ("Condición del Alunmo\n")
    nota=float(input("Indique su promedio: "))
    print(calcularEstadoAlumAux(nota))


##############################################################################


    
##############################################################################
def opcionPrimo():  #Llamará a una función recursiva
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Indica el valor booleano si el número es primo o no 
    """
    print ("\n------------------------\n")
    print ("Prueba del número primo\n")
    n = int(input("Ingrese n : "))
    print(str(n) + " es primo? " + str(esPrimo(n))) 

def opcionPotencia():   #Llamará a una función recursiva
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Texto completo que indica la potencia de un número. 
    """
    print ("\n------------------------\n")
    print ("Prueba de la potencia")
    a = int(input("Ingrese base : "))
    b = int(input("Ingrese exponente : "))
    print (str(a) + " elevando a la " +str(b) + " es " + str(potencia(a,b)))
##############################################################################


    
##############################################################################
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print ("\n**************************\n")
    print ("Práctica de Funciones")
    print ("\n**************************\n")
    print ("1. Año Bisiesto")
    print ("2. Recta Numérica")
    print ("3. Aumento de tarifa de buses")
    print ("4. IMC")
    print ("5. Tabla de multiplicar")#
    print ("6. Rango de tablas de multiplicar")#
    print ("7. Suma acumulada")#
    print ("8. Tipos de triángulo")#
    print ("9. Multiplicación correcta")#
    print ("10. Estado del alumno")#
    print ("0. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=10:   #ojo
        if opcion == 1:
            opcionBisiesto()
        elif opcion == 2 :
            opcionMasCercanos()
        elif opcion == 3:
            opcionAumentoTar()
        elif opcion == 4:
            opcionImc()
        elif opcion == 5:
            opcionTablaMult()
        elif opcion == 6:   
            opcionRangoMult()    
        elif opcion == 7:   
            opcionSumatoria()
        elif opcion == 8:
            opcionTipoTri()
        elif opcion == 9:
            opcionMultiCorrect()
        elif opcion == 10:
            opcionEstadoAlum()
        else:
            return
    else:
        print ("Opción inválida")
    menu()


#inicio del Programa Principal
menu()