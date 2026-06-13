from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import time
import random

# Tu API de la Pizzería que ya conocemos
app = FastAPI(title="Pizzería ML - Monitoreada Automatizada")

class PedidoPizza(BaseModel):
    queso_extra: int
    pepperoni: int
    pina: int

@app.post("/predecir")
def predecir_gusto(pedido: PedidoPizza):
    # Simulamos el tiempo de procesamiento del modelo (Latencia)
    time.sleep(random.uniform(0.1, 0.4)) 
    
    if pedido.pina == 1:
        return {"le_gustara_la_pizza": 0, "mensaje_del_chef": "Con piña no camina este modelo."}
    return {"le_gustara_la_pizza": 1, "mensaje_del_chef": "Combinación perfecta aprobada."}

# ¡Aquí activamos los sensores para que Prometheus pueda leer las métricas!
Instrumentator().instrument(app).expose(app)
