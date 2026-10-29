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

### Termux 

- **Сервер**
В терминале pts/0 подымаем сервер локальной нейросети 

```bash 

proot-distro login ubuntu && ollama serve &

```

<details>
<summary><b>pts/0</b></summary>
<img width="1200" height="1920" alt="1205" src="https://github.com/user-attachments/assets/56ce1d76-4026-45c1-bc30-dd87a6b251c0" />

</details>

- **Клиент**
В терминале pts/1 отправляем запрос на сервер

```python

python client.py

```

<details>
<summary><b>pts/1</b></summary>
<img width="1200" height="1920" alt="1206" src="https://github.com/user-attachments/assets/8a238484-9670-4fa2-b518-1cbfe3539aa9" />

</details>

Что ответила!? Это вопрос 10. Главное в формате json и мы видим что ловить чтоб строить цепочку для одгого ИИ-агента дальше. 

### Linux

На Linux другая система по сравнению с Termux. Ollama сервер всегда слушает 11434 порт.

<details>
<summary><b>ss</b></summary>
<img width="1905" height="741" alt="Снимок экрана от 2026-10-28 18-38-39" src="https://github.com/user-attachments/assets/ace9d52f-6fb9-4d33-a5fe-ab6b8fbbfb5f" />

</details>

<details>
<summary><b>python client.py</b></summary>
<img width="1860" height="1107" alt="Снимок экрана от 2026-10-28 18-36-05" src="https://github.com/user-attachments/assets/b6ff201f-f9a5-4286-8fd6-2363992b67a1" />

</details>

Система просыпается. Ответ интересный. Формирование формата JSON критически важно, особенно если архитектура автоматизации состоит из нескольских Агентов. Важна точка старта, запуск. 


