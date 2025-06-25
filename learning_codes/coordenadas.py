import requests
import time

response = requests.get("https://www.astroviewer.net/iss/en/")
#print(response.headers.get('Content-Type'))
coordenadas = response.json
#inicio = coordenadas.find("N (0°)") # Nos posicionamos justo después de "aquí"
#fin = coordenadas.find("(337.5°)")  # Posición donde empieza "pero"
#coordenadas_final = coordenadas[5964:6152].strip()
#print(inicio)
print(coordenadas)

