# ##########################
# #### Clase Dia 2 ######
# ##########################
#verificar si un numero es primo 
#entrada: vericar un numero primo 
#salida: verificacion realizada 

#proceso 

print('Bienvenido al portal para verificar si un numero es primo')

print('ingrese numero que desea verificar si es primo')
numVerificar=int(input())

divisores= 0
cantidadDivisores=0
for i in range(1,numVerificar,1):

    divisores= divisores +1

    resultado = numVerificar % divisores 

    if resultado == 0:
        cantidadDivisores = cantidadDivisores+1


if cantidadDivisores> 2:
        print('el numero no es primo')
    
else:
        print('el numero es primo')
        

# Desarrollado por Enrique Corpus - C.C.: 1.143.405.301