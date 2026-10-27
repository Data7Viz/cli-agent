import json
import ollama

# открываем импортированный файл выгружаем в переменн
with open("prompt_json", "r") as f:
    data=json.load(f)

# удаляем ключ схему '$schema': './schema_json'
data.pop("$schema", None)

# ручная передача параметров
# stream = ollama.chat(
#   model = data['model'],
#   messages['message'],
#   stream = True
#)

# передаём данные из JSON в OLLAMA
stream=ollama.chat(**data, stream=True)

# выводим на печать в цикле
for chunk in stream:
    print(chunk.message.content, end="", flush=True)

    # для ручной передачи параметров
    # print(chunk['message']['content'], end='', flu

