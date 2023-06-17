import urllib.parse
import requests


Pagina = "https://www.mapquestapi.com/directions/v2/route?"
key = "QXXwEmkrrPL0mBRFxL86l6Ae3tExiPu9"


while True:
    Comienzo = input ("Ubicación inicial: ")
    if Comienzo == "q":
        break
    Llegada = input ("Destino: ")
    if Llegada == "q":
        break
    url = Pagina + urllib.parse.urlencode ({"key" :key, "from" :Comienzo, "to" :Llegada, "locale" : "es_MX", "unit" :"k"})
    json_data = requests.get (url) .json ()
    
    print("Desde " + Comienzo + " hasta " + Llegada)
    print("Duración: " + (json_data["route"]["formattedTime"]))
    print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"]))) + "km")
    #print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    print("=============================================")
    for each in json_data ["route"] ["legs"] [0] ["maneuvers"]:
        print (((each) ["narrative"]) + "(" + str ("{:.2f}" .format (((each) ["distance"])) + "km)\n"))