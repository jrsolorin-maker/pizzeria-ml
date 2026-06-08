from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Pizzería ML - INFOTEP")

class PedidoPizza(BaseModel):
    queso_extra: int
    pepperoni: int
    pina: int

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a la Pizzería de Machine Learning! El horno está listo."}

@app.post("/predecir")
def predecir_gusto(pedido: PedidoPizza):
    if pedido.pina == 1:
        return {"le_gustara_la_pizza": 0, "probabilidad_de_exito": 0.95, "mensaje_del_chef": "Con piña no camina este modelo."}
    elif pedido.queso_extra == 1 and pedido.pepperoni == 1:
        return {"le_gustara_la_pizza": 1, "probabilidad_de_exito": 0.99, "mensaje_del_chef": "Combinación perfecta aprobada."}
    return {"le_gustara_la_pizza": 1, "probabilidad_de_exito": 0.70, "mensaje_del_chef": "Predicción calculada."}
