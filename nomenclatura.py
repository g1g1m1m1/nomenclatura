import json


data = json.load(open("json/output.json"))

lista = {}
lista["atomi"] = []

def svuota_json():
    del lista["atomi"]
    lista["atomi"] = []


def trova_no(no,elemento,tipo):
    ossidazione = no
    lista_no = []
    for i in elemento["numeri_ossidazione"]:
        try:
            n = i.split("+/-")
            if elemento["atomo"] == "zolfo" and int(n) == int(2):
                print("ok")
            else: 
                lista_no.append(int(n[1]))
        except:
            n = i
            lista_no.append(int(n))

        
    for i in elemento["numeri_ossidazione"]:
        try:
            try:
                n = i.split("+/-")
                if int(ossidazione) == int(n[1]):
                    ossidazione_real = ossidazione
            except:
                n = i
                if int(ossidazione) == int(n):
                    ossidazione_real = ossidazione
        except:
            pass
    if len(lista_no) == 1:
        suffisso = "di"
        if str(tipo) == "anidride":
            suffisso = "ica"
    elif int(ossidazione_real) == int(max(lista_no)):
        suffisso = "ico"
        if str(tipo) == "anidride":
            suffisso = "ica"
    elif int(ossidazione_real) == int(min(lista_no)):
        suffisso = "oso"
        if str(tipo) == "anidride":
            suffisso = "osa"
    else: 
        suffisso = "error"
        
    return suffisso



def trova_prefisso(tipo):
    tipo = tipo
    if str(tipo)=="idracido" or str(tipo)=="idruro":
        x = 1
    elif str(tipo)=="anidride" or str(tipo)=="ossido":
        x = 0

    ultimo = (len(str(lista["atomi"][x]["atomo"])))
    prefisso = (str(lista["atomi"][x]["atomo"])[0:int(ultimo-1)])
    if str(lista["atomi"][x]["atomo"]) == "Zolfo":
        if str(tipo)==str("idracido"):
            prefisso = "Solf"
        else:
            prefisso = "Solfor"
    elif str(lista["atomi"][x]["atomo"]) == "Azoto":
        prefisso = "Nitr"
    elif str(lista["atomi"][x]["atomo"]) == "Rame":
        prefisso = "Rame"
    elif str(lista["atomi"][x]["atomo"]) == "Carbonio":
        prefisso = "Carbon"


    return str(prefisso)

def anidride_nom(tipo):
    tipo = tipo
    prefisso = trova_prefisso(tipo)
    no_non_met = lista["atomi"][1]["numero_ossidazione"]
    suffisso = trova_no(no_non_met, lista["atomi"][0],tipo)
    output = "Anidride " + str(prefisso) + str(suffisso)
    svuota_json()
    return (output)
    
    

def ossido_nom(tipo):
    tipo = tipo
    prefisso = trova_prefisso(tipo)
    no_met = lista["atomi"][1]["numero_ossidazione"]
    suffisso = trova_no(no_met, lista["atomi"][0],tipo)
    if str(suffisso)==str("di"):
        output = "Ossido "+"di "+lista["atomi"][0]["atomo"]
    else:
        output = "Ossido " + str(prefisso) + str(suffisso)
    svuota_json()
    return (output)


def idruro_nom(tipo):
    tipo = tipo
    prefisso = trova_prefisso(tipo)
    no_met = lista["atomi"][1]["numero_ossidazione"]
    suffisso = trova_no(no_met, lista["atomi"][0],tipo)
    if str(suffisso)==str("di"):
        output = "Idruro "+"di "+lista["atomi"][0]["atomo"]
    else:
        output = "Idruro " + str(prefisso) + str(suffisso)
    svuota_json()
    return (output)

def idracido_nom(tipo):
    tipo = tipo
    no_met = lista["atomi"][1]["numero_ossidazione"]
    prefisso = trova_prefisso(tipo)
    output = "acido "+prefisso+"idrico"
    svuota_json()
    return (output)


def binary_nomenclatura():
    if str(lista["atomi"][1]["atomo"]) == "Ossigeno":
        if str(lista["atomi"][0]["tipo"]) == "Altro" or str(lista["atomi"][0]["tipo"]) == "Semimetallo":
            #print("Anidride")
            return anidride_nom("anidride") 
        elif str(lista["atomi"][0]["tipo"]) == "Metallo di transizione" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino-terroso" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino":
            #print("ossido")
            return ossido_nom("ossido")
    elif str(lista["atomi"][1]["atomo"]) == "Idrogeno":
        if str(lista["atomi"][0]["tipo"]) == "Metallo di transizione" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino-terroso" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino":
            #print("Idruro")
            return idruro_nom("idruro")
    elif str(lista["atomi"][0]["atomo"]) == "Idrogeno":
        if str(lista["atomi"][1]["tipo"]) == "Altro" or str(lista["atomi"][1]["tipo"]) == "Semimetallo":
            #print("Idracido")
            return idracido_nom("idracido")
    elif str(lista["atomi"][0]["tipo"]) == "Metallo di transizione" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino-terroso" or str(lista["atomi"][0]["tipo"]) == "Metallo alcalino":
        if str(lista["atomi"][1]["tipo"]) == "Altro" or str(lista["atomi"][1]["tipo"]) == "Semimetallo":
            print("sale binario")
            #sale_binario_nom()
    else: 
        return "error"
    
def main(value):
    #value = input(": ")
    inp = value.split(" ")
    for x in range(len(inp)):
        for i in range(109):
            if str(inp[x])==str(data["atomi"][i]["simbolo"]):
                #print(data["atomi"][i]["nome"])
                lista["atomi"].append({
                    "atomo":str(data["atomi"][i]["nome"]),
                    "numero_atomi": int(1),
                    "numero_ossidazione":"",
                    "numeri_ossidazione":str(data["atomi"][i]["numeri di ossidazione"]).split(", "),
                    "tipo":data["atomi"][i]["tipo"],
                    })
            else:
                try:
                    inp2 = inp[x].split("_")
                    if str(inp2[0])==str(data["atomi"][i]["simbolo"]):
                        #print(data["atomi"][i]["nome"],inp2[1]) 
                        lista["atomi"].append({
                            "atomo":data["atomi"][i]["nome"],
                            "numero_atomi":int(inp2[1]),
                            "numero_ossidazione":int(inp2[1]),
                            "numeri_ossidazione":data["atomi"][i]["numeri di ossidazione"].split(", "),
                            "tipo":data["atomi"][i]["tipo"],
                            })                          
                except:
                    pass

    #print(json.dumps(lista,indent=4))   

    if len(inp) == 2:
        try:
            return binary_nomenclatura()
        except:
            return "error"    
    else: 
        return "error"

def start(x):
    if x["molecola"].split("_"):
        return main(x["molecola"])
    else:
        return "error"