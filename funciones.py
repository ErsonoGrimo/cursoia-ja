from datetime import datetime

import os
import config
from functions import chat,funciones

import streamlit as st

os.environ["OPENAI_API_KEY"] = config.KEY

def fechahoy ():
    return datetime.now().strftime('%d/%m/%Y')

mensaje = "ha que estamos hoy?"
st.text(mensaje)
messages=[
              {"role": "system", "content": "Eres un asistente para indicar la mejor funcion para ejecutar la tarea que pide el usuario"},
              {"role": "assistant", "content": " ¿Buenos dias en que te puedo ayudar?"},
              {"role": "user", "content": mensaje}
              ]

respuesta = funciones(messages)

if respuesta.finish_reason == "function_call":
    fecha = fechahoy()
    messages.append(respuesta.message)
    messages.append({"role":"function","content":fecha,"name":"fechahoy"})
    respuesta = funciones(messages)

st.text(respuesta.message.content)