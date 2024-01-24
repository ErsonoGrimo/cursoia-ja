
import os
import config
from functions import create_thread, ezbirros
os.environ["OPENAI_API_KEY"] = config.KEY


asistentecobol = ezbirros("Asistente Cobol Tabla DB2","gpt-3.5-turbo-1106", """Actúa como si fueras un Analista Programador, con conocimientos avanzados en DB2 para Mainframe de IBM
Crea el código SQL, necesario, para crear  una Tabla DB2 con su índice principal y único.""")