# ##########################
# #### Clase Dia 7 ######
# ##########################
from funcionesLista import *
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[
        {
            "codigo":57,
            "numero":3023019865,
            "tipo":"trabajo"
        },
        {
            "codigo":1,
            "numero":3983054625,
            "tipo":"personal"
        }
    ]
}

diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
userCant = 2
booleanito = True
while(booleanito):
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
        # receceocuón de dati¿os de usuarios
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
        print(' ')
        userCant += 1 
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
    elif(opcionUsuario==5):
        print("#################")
        print("#### Eliminar Persona Individual ####")
        print("#################")
        recorrerLista(listaRobusta)
        opcionIndividual = int(input("Por favor ingresar el numero de la persona a eliminar:"))
        mostrarUna(listaRobusta,opcionIndividual)
        opcionIndividual = int(input("¿Estás seguro de eliminar a esta persona? (1.Si,2.No):"))
        if (opcionIndividual==1):
            listaRobusta.pop(opcionIndividual-1)
            print("Usuario eliminado!")
        else:
            print("Gracias por confirmar!")
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")
#Desarrollado por Pedro Felipe Gómez : C.C-1.555.444.333