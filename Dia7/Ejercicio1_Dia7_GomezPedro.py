# ##########################
# #### Clase Dia 7 ######
# ##########################

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
    print(listaRobusta)
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
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")
    elif(opcionUsuario==3):
        print("#################")
        print("#### Buscar Persona Individual ####")
        print("#################")
        opcionIndividual = int(input("Por favor ingresar el ID de la persona deseada:"))
        print("#################")
        print("#### Persona #",opcionIndividual," ####")
        print("#################")
        print("ID:", listaRobusta[opcionIndividual-1]["id"])
        print("Nombre:",listaRobusta[opcionIndividual-1]["nombre"])
        print("Apellido:",listaRobusta[opcionIndividual-1]["apellido"])
        print("Edad",listaRobusta[opcionIndividual-1]["edad"])
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Pedro Felipe Gómez : C.C-1.555.444.333