from datetime import datetime

import json
import os
import config
from functions import chat,funciones

import streamlit as st

os.environ["OPENAI_API_KEY"] = config.KEY

def fechahoy ():
    return datetime.now().strftime('%d/%m/%Y')

def generaFichero (nombrefichero):
    open(nombrefichero, "x")
    return "Creado fichero " + nombrefichero

mensaje = st.text_input("¿En que te puedo ayudar?")


if mensaje:

    messages=[
                {"role": "system", "content": "Eres un asistente para indicar la mejor funcion para ejecutar la tarea que pide el usuario"},
                {"role": "assistant", "content": " ¿Buenos dias en que te puedo ayudar?"},
                {"role": "user", "content": mensaje}
                ]

    functions = [
                {"name":"fechahoy",
                "description":"Recupera la fecha de hoy",
                "parameters":{
                    "type":"object",
                    "properties":{}
                    }
                },
                {"name":"generaFichero",
                "description":"Genera un fichero .txt",
                "parameters":{
                    "type":"object",
                    "properties":{
                            "nombrefichero":{
                                "type": "string",
                                "description": "nombre del fichero",
                            }
                    }
                    }
                }
                ]

    respuesta = funciones(messages,functions)

    if respuesta.finish_reason == "function_call":
        nombre_funcion = respuesta.message.function_call.name
        st.text(nombre_funcion)
        if  nombre_funcion =="generaFichero":
            propiedades = json.loads(respuesta.message.function_call.arguments)
            namefichero = propiedades["nombrefichero"]
            fichero = generaFichero(namefichero)
            messages.append(respuesta.message)
            messages.append({"role":"function","content":fichero,"name":"generaFichero"})
            respuesta = funciones(messages,functions)

        if nombre_funcion =="fechahoy":
            fecha = fechahoy()
            messages.append(respuesta.message)
            messages.append({"role":"function","content":fecha,"name":"fechahoy"})
            respuesta = funciones(messages,functions)
    

    st.text(respuesta.message.content)