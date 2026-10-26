# JSON Network

## Содержимое конфигурации
- **network.json** Сеть ip адес, порт, эндпоинт, API.
- **prompt.json** Управление автоматизацией.
- **schema.json** Подсказки, автодополнение, проверяет синтаксис.

## Среда разработки 
- **Linux / Termux** терминал.
- **Nvim** LSP. 
- **Ollama** локальная нейросеть (qwen2.5-coder:7b).

---
---

## schema.json
Без автодополнения и подсказок вникать в JSON сложно. Содержимое файла schema.json сгенерировал браузерный ИИ. Практиковаться буду через curl. 

---
---

## prompt.json

<details>
<summary><b>Смотреть первый запуск через curl</b></summary>
<img width="1877" height="1076" alt="Снимок экрана от 2026-10-25 14-08-56" src="https://github.com/user-attachments/assets/1655ebd3-052f-47e5-aa62-2d63c354799e" />

</details> 
Много мусора нейросеть выводит по слогам.

---
---

## Роль системы: программист на Си

<details>
<summary><b>Смотреть Промт</b></summary>

```
{
	"$schema": "./schema.json",
	"model": "qwen2.5-coder:7b",
	"messages": [
		{
			"role": "system",
			"content": "Ты программист на языке программирования Си"
		},
		{
			"role": "user",
			"content": "Кто ты?"
		}
	],
	"seed": 0,
	"stream": false
}

```
</details> 

<details>
<summary><b>Смотреть Ответ нейрона</b></summary>
<img width="1900" height="646" alt="Снимок экрана от 2026-10-25 18-36-10" src="https://github.com/user-attachments/assets/61c2b506-a875-44ef-9ac9-191d685d8545" />

</details>

Рабочий движок на семь миллиардов весов 4 запроса. Модель не такая большая возможно поэтому ответ локальной нейросети неоднозначный. 

### Цель впоймать логику локального нейрона на 7b

---
---

## Cэмулировал прошлое общение

</details>

<details>
<summary><b>Смотреть промт</b></summary>

```
{
	"$schema": "./schema.json",
	"model": "qwen2.5-coder:7b",
	"messages": [
		{
			"role": "system",
			"content": "Ты виртуальный исполнитель команд в системе Linux. Ты выполняешь команды и выводишь результат работы"
		},
		{
			"role": "user",
			"content": "Проверка связи"
		},
		{
			"role": "assistant",
			"content": "Твой виртуальный исполнитель команд готов к работе"
		},
		{
			"role": "user",
			"content": "ss -t"
		}
	],

	"stream": false,
	"options": {
		"temperature": 0.0,
		"seed": 0
	}
}

```
</details>

<details>
<summary><b>Смотреть Ответ нейрона</b></summary>
<img width="1918" height="1110" alt="Снимок экрана от 2026-10-25 21-20-36" src="https://github.com/user-attachments/assets/f8c92ae7-1900-4b48-aa65-23b9b68a873a" />

</details>

Команда ls нейрон вывел директории домашней папки. Запрос отправлял с директории: 
- **neur ~/cli-agent/config** 
- **$ ls network.json  prompt.json  README.md  schema.json**

Команда ss -t. В начале sudo ss -t. Потом промт. Потом запрос через curl. Ответ что-то не понятное.

### Момент истины
Я ожидаю выполнение программ ( ss, ls ). Программы выполняться в данном случае не могут. 
