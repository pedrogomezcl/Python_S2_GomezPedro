# ##########################
# #### Clase Dia 9 ######
# ##########################
from funciones.funcionesLista import *
from funciones.funcionesGGDD import *

listaRobusta = abrirJSON()
booleanito = True

while(booleanito):
    listaRobusta=abrirJSON()
    print(type(listaRobusta))
    #print(listaRobusta)
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        # Obtener datos del nuevo usuario
        nombre = input('Por favor, ingrese el nombre: ')
        apellido = input('Por favor, ingrese el apellido: ')
        edad = int(input('Por favor, ingrese el edad: '))
        canTelefono = int(input('Por favor, ingrese la cantidad de telefonos: '))
        diccionarioUsuario={
            "id": (listaRobusta[len(listaRobusta)-1]["id"])+1,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "telefonos": []
        }
        for i in range(canTelefono):
            codigo = int(input('Por favor, ingrese el codigo: '))
            numero = int(input('Por favor, ingrese el numero: '))
            tipo = input('Por favor, ingrese el tipo de telefono:' )
            data_telefono = {
                "codigo": codigo,
                "numero": numero,
                "tipo": tipo
            }
            diccionarioUsuario['telefonos'].append(data_telefono)
        listaRobusta.append(diccionarioUsuario)
        guardarJSON(listaRobusta)
        print(' ')
        
        # userCant = userCant + 1
        print(f'Persona {nombre} fue creada exitosamente.')
    elif(opcionUsuario==2):
        recorrerLista(listaRobusta)
    elif(opcionUsuario==3):
        print("#################")
        print("#### Buscar Persona Individual ####")
        print("#################")
        opcionIndividual = int(input("Por favor ingresar el numero de la persona deseada:"))
        mostrarUna(listaRobusta,opcionIndividual)
    elif(opcionUsuario==4):
        print("#################")
        print("#### Actualizar Persona Individual ####")
        print("#################")
        opcionIndividual = int(input("Por favor ingresar el numero de la persona deseada:"))
        mostrarUna(listaRobusta,opcionIndividual)
        usuarioTemporal = listaRobusta[opcionIndividual-1] #Estoy guardando el usuario a modificar
        nombreTemporal= input("¿Cuál es el nombre que quieres poner?:")
        apellidoTemporal=input("¿Cuál es el apellido que quieres poner?:")
        edadTemporal=input("¿Cuál es la edad que quieres poner?:")
        cantTelefonos= int(input("¿Cuántos teléfonos vas a agregar?"))
        listaTelefonosTemporal=[]
        for i in range(cantTelefonos):
            areaTelefono=int(input(f'¿Cuál es la área del teléfono # ${i+1}?:'))
            telefonoIngresado=int(input(f'¿Cuál es el teléfono # ${i+1}?:'))
            tipoTelefono=int(input(f'¿Cuál es el tipo del telefono # ${i+1}?(1.Personal,2.Trabajo)'))
            if(tipoTelefono==1):
                diccionarioTemporal={
                    "codigo":areaTelefono,
            "numero":telefonoIngresado,
            "tipo":"personal"
                }
                listaTelefonosTemporal.append(diccionarioTemporal)
            elif(tipoTelefono==2):
                diccionarioTemporal={
                    "codigo":areaTelefono,
            "numero":telefonoIngresado,
            "tipo":"trabajo"
                }
                listaTelefonosTemporal.append(diccionarioTemporal)
        diccionarioAgregar={"id":listaRobusta[opcionIndividual-1]["id"],"nombre":nombreTemporal,"apellido":apellidoTemporal,"edad":edadTemporal,"telefonos":listaTelefonosTemporal}
        listaRobusta[opcionIndividual-1]=diccionarioAgregar
        guardarJSON(listaRobusta)
    elif(opcionUsuario==5):
        print("#################")
        print("#### Eliminar Persona Individual ####")
        print("#################")
        recorrerLista(listaRobusta)
        opcionIndividual = int(input("Por favor ingresar el numero de la persona a eliminar:"))
        mostrarUna(listaRobusta,opcionIndividual)
        opcionIndividual2 = int(input("¿Estás seguro de eliminar a esta persona? (1.Si,2.No):"))
        if (opcionIndividual2==1):
            temporal= listaRobusta.pop(opcionIndividual-1)
            logsJSON(temporal)
            #print(temporal)
            guardarJSON(listaRobusta)
            print("Usuario eliminado!")
        else:
            print("Gracias por confirmar!")
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")
#Desarrollado por Pedro Felipe Gómez : C.C-1.555.444.333