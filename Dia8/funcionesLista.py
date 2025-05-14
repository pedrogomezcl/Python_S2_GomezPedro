def recorrerTelefonos(lista,posicion):
    posicion -=1
    for q in range(len(lista[posicion]["telefonos"])):
                print("---------------------------")
                print("Telefonossss#",q+1,":")
                print("#### - Código:",lista[posicion]["telefonos"][q]["codigo"])
                print("#### - Numero:",lista[posicion]["telefonos"][q]["numero"])
                if(lista[posicion]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
    return lista[posicion]["telefonos"]
def recorrerLista(listaRobusta):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            listaTelefonos=recorrerTelefonos(listaRobusta,i)
                
            print("---------------------------")
def mostrarUna(listaRobusta,opcionIndividual):
    print("#################")
    print("#### Persona #",opcionIndividual," ####")
    print("#################")
    print("ID:", listaRobusta[opcionIndividual-1]["id"])
    print("Nombre:",listaRobusta[opcionIndividual-1]["nombre"])
    print("Apellido:",listaRobusta[opcionIndividual-1]["apellido"])
    print("Edad",listaRobusta[opcionIndividual-1]["edad"])
    listaTelefonos=recorrerTelefonos(listaRobusta,opcionIndividual)