import requests
import json
from datetime import datetime

def obtener_datos_litoral():
    # Estructura base de datos para Concordia y la región
    datos = {
        "fecha_actualizacion": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "oni": 0.7, # Valor de anomalía del Pacífico (Simulado)
        "caudal_br": 11500, # Caudal de aporte Salto Grande (m3/s)
        "puertos": [
            {"nombre": "Concordia", "nivel": 6.20, "tendencia": "Ascenso"},
            {"nombre": "Colón", "nivel": 4.15, "tendencia": "Estacionario"},
            {"nombre": "C. del Uruguay", "nivel": 2.85, "tendencia": "Descenso"}
        ]
    }
    
    # Guardamos el JSON que lee tu index.html
    with open('data.json', 'w') as f:
        json.dump(datos, f, indent=4)
    print("Base de datos regional actualizada.")

if __name__ == "__main__":
    obtener_datos_litoral()
