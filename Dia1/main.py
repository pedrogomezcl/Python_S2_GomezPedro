# ##########################
# #### Clase Dia 1 ######
# ##########################

#Imprimir en Pitón
print("Hola Mundo!")

#Creación de variables
#1. Dato tipo string
nombre = "Pedro"
print(type(nombre))
#2. Dato tipo numero entero
numeroEntero=5
print(numeroEntero)
print(type(numeroEntero))
#3. Dato tipo numero real
numeroReal = 5.3
print(type(numeroReal))
#4. Dato tipo double
numeroPi=3.14163456789098765434567890
print(numeroPi)
#5. Dato tipo booleano
booleanito = True
print(booleanito)
#6. (SOLO PYTHON) Numero complejo
numeroComplejo= complex('+1.23')
print(numeroComplejo)
print(type(numeroComplejo))
# ##########################

#Convertir numero int a float
numeroNuevo = float(numeroEntero)
print(numeroNuevo)
print(" ")

# ##########################
#Ciclo for (Hasta)
for i in range(5):
    print(i)
print(" ")
#Ciclo for (Desde- Hasta)
for i in range(0,5):
    print(i)
print("")
for i in range(1,5):
    print(i)
print("")
#Ciclo for (Desde-Hasta-Paso)
for i in range(1,5,1):
    print(i)
# ##########################
#Ciclo While
booleanitoNuevo = True
while(booleanitoNuevo==True):
    print("Sigo siendo verdadero!!!!!")
    booleanitoNuevo=False

booleanitoNuevo = True
while(booleanitoNuevo):
    print("Sigo siendo verdadero!!!!!")
    booleanitoNuevo=False

print(" ")
# ##########################
# Condicionales if-else
texto="Pedro"
if(texto=="Corpus"):
    print("Sos corpus :yay:")
else:
    if(texto=="Sharick"):
        print("Sos Sharick :yay:")
    else:
        print("No sos ninguno :sadfeis:")

# Condicionales elif
if(texto=="Corpus"):
    print("Sos corpus :yay:")
elif(texto=="Sharick"):
    print("Sos Sharick :yay:")
else:
    print("No sos ninguno :sadfeis:")
# ##########################
# Anidar condicionales
booleanitoCorpus1= True
booleanitoCorpus2= False
if(booleanitoCorpus1==True and booleanitoCorpus2==True):
    print("Todos somos verdaderos :3 :uwu:")
else:
    print("No somos iguales :(")
# ##########################
# Entradas de usuario
nombreUsuario= input("¿Cuál es tu nombre?:") ##Todos los inputs son String
print("Tu nombre es:"+nombreUsuario)#Concatenación
#Casteo de String a numero
edadUsuario=int(input("¿Cual es tu edad?:"))
edadUsuario = edadUsuario + 5
print("La edad de "+nombreUsuario+" es de:"+str(edadUsuario))
# ##########################
#Funciones
#1. Función con retorno y con parámetros
def areaCirculo(radio):
    valorPi=3.1416
    resultadoFinal = valorPi * (radio**2)
    return resultadoFinal
radioUsuario=float(input("¿Cuál es el radio de su circulo?:"))
print("El área del circulo es de:"+str(int(areaCirculo(radioUsuario))))
#2. Funcion con retorno y sin parámetros
def valorDolar():
    return 4299
valorFinalDolar=valorDolar()
print("El valor del dólar es:"+str(valorFinalDolar))
#3. Función sin retorno y con parámetros
def concatenarNombres(nombre,apellido):
    print("Su nombre completo es:"+nombre+" "+apellido)
concatenarNombres("Sharick","Ibañez")
#4. Función sin retorno y sin parámetros
def funcionX():
    print("Soy una función que solo vive y existe")
funcionX()
# Desarrollado por : Pedro Felipe Gómez Bonilla - C.C:1.777.666.555