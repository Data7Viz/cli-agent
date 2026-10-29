import json
import ollama
def debug_step(response, raw_content):
    """Временная функция отладки. Вывел на печать — посмотрел — удалил."""
    try:
        import json
        clean_json = json.loads(raw_content)
        print(f" {response.message.content}")
        if isinstance(clean_json, dict) and clean_json:
            if "error" in clean_json:
                print(f"Контент (Ошибка): {clean_json['error']}")
            else:
                print(f"Контент (Успех): {list(clean_json.values())}")
        else:
            print(f"Контент: {clean_json}")
    except Exception:
        print(f"Роль: {response.message.role}")
        print(f"Контент (Сырой текст): {raw_content}")
    print("-" * 30)


# 1. Создаем клиентов для разных серверов
client_local_1 = ollama.Client(host="http://127.0.0.1:11434")
client_local_2 = ollama.Client(host="http://127.0.0.1:11435")
client_tablet = ollama.Client(host="http://192.168.1.50:11434")

# 2. Читаем промпт и конфигурацию из JSON
with open("prompt.json", "r") as f:
    data = json.load(f)

data.pop("$schema", None)

data["format"] = "json"

# 3. Отправляем запрос (СТРИМИНГ ВЫКЛЮЧЕН: stream=False)
response = client_local_1.chat(**data, stream=False)

# 4. Ловим сырой ответ ассистента (строку) из объекта Ollama
raw_content = response.message.content or ""

try:
    # 5. Превращаем её в чистый JSON объект
    clean_json = json.loads(raw_content)
    
    debug_step(response, raw_content)
    # Дальше clean_json идет в твою цепочку без всяких принтов!

except json.JSONDecodeError:
    print("Модель вернула обычный текст вместо JSON. Сырой текст:")
    print(raw_content)

