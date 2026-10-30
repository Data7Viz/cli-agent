import json
import ollama

# 1. Создаем клиентов для разных серверов
client_local_1 = ollama.Client(host="http://127.0.0.1:11434")
client_local_2 = ollama.Client(host="http://127.0.0.1:11435")
client_tablet = ollama.Client(host="http://192.168.1.50:11434")

# 2. Читаем промпт и конфигурацию из JSON
with open("prompt.json", "r") as f:
    data = json.load(f)

# удаляем метаданные 
data.pop("$schema", None)

# формируем JSON 
data["format"] = "json"

# передаём управление на локальный сервер
response = client_local_1.chat(**data, stream=False)

# 4. Ловим сырой ответ от Ollama
raw_content = response.message.content or ""

try:
    # 5. Превращаем её в чистый JSON объект
    clean_json = json.loads(raw_content)
    print(clean_json)
    res = clean_json.get("result") 
    print(res)   

except json.JSONDecodeError:
    print("Модель вернула обычный текст вместо JSON. Сырой текст:")
    print(raw_content)

