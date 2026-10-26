import json
import requests  # Вместо ollama используем стандартные HTTP-запросы

# 1. Читаем ваш JSON-файл с промптом
with open("prompt.json", "r") as f:
    data = json.load(f)

# Убираем ключ автодополнения
data.pop("$schema", None)

# 2. УПРАВЛЕНИЕ АДРЕСОМ, ПОРТОМ И ЭНДПОИНТОМ 
HOST = "localhost"
PORT = "11434"
ENDPOINT = "/api/chat"

url = f"http://{HOST}:{PORT}{ENDPOINT}"

# 3. Отправляем POST-запрос с флагом потока (stream=True)
response = requests.post(url, json=data, stream=True)

# 4. Построчно читаем сырой ответ из сетевого сокета
for line in response.iter_lines():
    if line:
        # Сервер Ollama на каждый кусок присылает чистую строку JSON. Парсим её:
        chunk = json.loads(line.decode("utf-8"))
        
        # Печатаем текст. При работе через requests структура ответа выглядит так:
        print(chunk["message"]["content"], end="", flush=True)

