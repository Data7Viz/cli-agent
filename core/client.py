import json
import ollama

# открываем импортированый файл выгружаем в переменную data 
with open("prompt.json", "r") as f:
    data=json.load(f)

# передаём данные из JSON а OLLAMA 
stream=ollama.chat(**data, stream=True) 

# выводим на печать в цикле 
for chunk in stream:
    print(chunk.message.content, end="", flush=True) 
