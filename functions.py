from openai import OpenAI

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


def funciones (messages):
    client = OpenAI()   
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=400,
        temperature=0.7,
        messages= messages,
        functions=[
              {"name":"fechahoy",
               "description":"Recupera la fecha de hoy",
               "parameters":{
                   "type":"object",
                   "properties":{}
                }
              }
             ]
    )
    return (chat.choices[0]) 