import json
import ollama

# открываем импортированый файл выгружаем в переменную data 
with open("prompt.json", "r") as f:
    data=json.load(f)

# удаляем ключ схему "$schema": "./schema.json"
data.pop("$schema", None)

# ручная передача параметров
# stream = ollama.chat(
   # model = data ["model"],
   # messages["message"],
   # stream = True
#)

# передаём данные из JSON а OLLAMA 
stream=ollama.chat(**data, stream=True) 

# выводим на печать в цикле 
for chunk in stream:
    print(chunk.message.content, end="", flush=True) 
    
    # для ручной передачи параметров
    # print(chunk["message"]["content"], end="", flush=True)
