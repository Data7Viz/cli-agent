# Структура Ядра / core

- **client.py** ollama это сервер client.py это клиент. Клиент серверная архитектура. Клиент это тот кто кричит Сервер это тот кто слушвет. Здесь библиотека ollama всё скрыто. Закоментировал ручной разбор параметров.
- **client_requ.py** тот же Сервер но на библиотеке **reqwest** здесь ты видишь контролируешь порт, адрес и т.д. 
- **schema.json** автодополнение, подсказки JSON для формирования промта.
- **prompt.json** запрос на сервер. 

### Развернуть локальную нейросеть я имею ввиду сто двадцать седьмой адрес. Веса ложу в оперативную память. 

## client.py строим цепочку ИИ-агента

Сделал запрос в нейросеть. Получил ответ и вывел на печать. Для разработки  ИИ-агента эти принты нужны для контроля. Выводить на печать нужно в JSON. Увидел что и как ответил нейрон print можно удалять. И строить цепочку дальше.

<details>
<summary><b>Код</b></summary>

```python

import json
import ollama

# 1. Создаем клиентов для разных серверов
client_local_1 = ollama.Client(host="http://127.0.0.1:11434")
client_local_2 = ollama.Client(host="http://127.0.0.1:11435")
client_tablet = ollama.Client(host="http://192.168.1.50:11434")

# 2. Читаем промпт и конфигурацию из JSON
with open("prompt.json", "r") as f:
    data = json.load(f)

data.pop("$schema", None)

# --- ИЗМЕНЕНИЯ ЗДЕСЬ ---

# 3. Отправляем запрос (СТРИМИНГ ВЫКЛЮЧЕН: stream=False)
response = client_local_1.chat(**data, stream=False)

# 4. Ловим сырой ответ ассистента (строку) из объекта Ollama
raw_content = response.message.content

try:
    # 5. Превращаем её в чистый JSON объект
    clean_json = json.loads(raw_content)

    # 6. Выводим на печать КРАСИВЫЙ ЧИСТЫЙ JSON для дебага
    print(json.dumps(clean_json, ensure_ascii=False, indent=4))

    # Дальше clean_json идет в твою цепочку без всяких принтов!

except json.JSONDecodeError:
    print("Модель вернула обычный текст вместо JSON. Сырой текст:")
    print(raw_content)

raw_string_output = response['message']['content']
clean_json = json.loads(raw_string_output)
# Всё, данные ушли следующему звену без вывода на экран!

```

</details> 
