from openai import OpenAI
from openai import Client

def chat (mensaje):
    client = OpenAI()   
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=400,
        temperature=0.7,
        messages=[
              {"role": "system", "content": "Comportate como un Analista Programador en lenguaje COBOL en entornos Mainframe, las respuestas deben ser técnicas pero con tono divertido"},
              {"role": "assistant", "content": "Buenos dias querido Ezbirro! ¿que quieres saber sobre COBOL?"},
              {"role": "user", "content": mensaje}
              ]
    )
    return (chat.choices[0].message.content)


def funciones (messages,functions):
    client = OpenAI()   
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=400,
        temperature=0.7,
        messages= messages,
        functions=functions
    )
    return (chat.choices[0]) 

def ezbirros(nombre,modelo,instrucciones):
    client = Client()
    assistant = client.beta.assistants.create(
        name=nombre,
        model=modelo,
        instructions=instrucciones
    )
    return assistant

def create_thread():
    client = Client()
    thread = client.beta.threads.create()
    print("Thread created, id: ", thread.id)
    return thread