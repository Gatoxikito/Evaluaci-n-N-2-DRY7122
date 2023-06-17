import requests
host = "https://sandboxdnac2.cisco.com"
auth = "/dna/system/api/v1/auth/token"
head = {"Content-Type" : "application/json",
        "Authorization" : "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="
        }
token = requests.post(url=host+auth, headers=head, verify=False)
token = token.json()["Token"]




head2 = {"Content-Type" : "application/json",
        "x-auth-token" : token
        }

Consulta = "/dna/intent/api/v1/network-device"
Dispositivos = requests.get(url=host+Consulta, headers=head2, verify=False)
Dispositivos = Dispositivos.json()

for z in Dispositivos["response"]:
    print(f" El dispositivo {z['hostname']}, tiene la ip de administración {z['managementIpAddress']}")