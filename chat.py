import os
import config
from functions import chat,funciones

import streamlit as st

os.environ["OPENAI_API_KEY"] = config.KEY

mensaje = "Sentencia MOVE"
respuesta = chat(mensaje)
st.text(respuesta)





