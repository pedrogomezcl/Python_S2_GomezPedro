import json

def abrirJSON():
    dicFinal=[]
    with open("./data/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./data/datos.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs():
    dicFinal=[]
    with open("./data/logs.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def logsJSON(dic):
    dicTemporal = []
    #print("Diccionario Importado LOGS")
    
    dicTemporal=cargarLogs()
    #print(dicTemporal)
    dicTemporal.append(dic)
    with open("./data/logs.json",'w') as outFile:
        json.dump(dicTemporal,outFile)