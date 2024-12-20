import requests

# URL del endpoint de Rasa (ajusta la URL si estás usando un servidor diferente)
url = "http://localhost:5005/webhooks/rest/webhook"

# Mensaje a enviar (ejemplo: saludo)
message = {"sender": "user1", "message": "Hola"}

# Enviar la solicitud POST
response = requests.post(url, json=message)

# Imprimir la respuesta del chatbot
print(response.json())
