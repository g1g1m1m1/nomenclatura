import json

data = json.load(open("elements.json"))
data2 = json.load(open("elements2.json"))

lista = {}
lista["atomi"] = []
for f in data2["PERIODIC_TABLE"]["ATOM"]:
    simbolo2 = f["SYMBOL"]
    for i in range(118):
        simbolo1 = (data[i]["symbol"])
        if str(simbolo1)==str(simbolo2):
            try:
                ossidazione = f["OXIDATION_STATES"]
            except:
                ossidazione = "error"
            lista["atomi"].append({
                "simbolo":(data[i]["symbol"]),
                "nome":(data[i]["name"]),
                "numeri di ossidazione":ossidazione,
                "tipo":(data[i]["type"])
                })
        else: 
            pass


    
with open('output.json', 'w') as outfile:
    json.dump(lista, outfile, indent=4)