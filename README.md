# cli-agent Нейросеть | ИИ-Агент 
Автоматизация = Нейросеть + Агент
- База данных
- Движок обучения
- На выходе файл с весами
- Рабочий движок
- Нейросеть
- Агент
- До обучение

## Рабочая среда Linux Tetmux 
Матрицы буду перемножать на процессоре

## ЦЕЛЬ: Развернуть локальную нейросеть
- Установить рабочий движок ollama **curl -fsSL https://ollama.com | sh** 
- Установить файл с весами (Linux оперативки 16Гб = 7b Termux 8Гб = 3b)
- **ollama pull qwen2.5-coder:7b** 
- Запукс **ollama run qwen2.5-coder:7b**

## Мониторинг локальной сети ноутбука
Установил движок + веса перезагрузил ноут.
Пошурудим битами по сети Утилиты: ss, nmap, curl. 

<details>
<summary><b>Смотреть -> ss -tlpn</b></summary>
<img width="1843" height="228" alt="Снимок экрана от 2026-10-21 13-51-56" src="https://github.com/user-attachments/assets/6f7692a4-6cd1-4855-840c-552847255aa8" />

</details>

Адрес 127.0.0.1 Порт 11434 Имя ollama

<details>
<summary><b>Смотреть -> nmap -p- 127.0.0.1</b></summary>
<img width="915" height="326" alt="Снимок экрана от 2026-10-21 14-09-24" src="https://github.com/user-attachments/assets/5c7e623e-e3aa-4587-9f64-5ea805bf19fd" />

</details>

Порт 11434 открыт сервис возможно nmap ни чего не знает об этом сервисе. Либо изменить опции.

<details>
<summary><b>Смотреть -> curl http://127.0.0.1:11434</b></summary>
<img width="1107" height="162" alt="Снимок экрана от 2026-10-21 14-21-32" src="https://github.com/user-attachments/assets/c9588fdd-d991-4351-8fa2-1d56733c3fe1" />

</details>

<details>
<summary><b>Смотреть -> поисковик браузер http://127.0.0.1:11434</b></summary>
<img width="1912" height="308" alt="Снимок экрана от 2026-10-21 14-35-04" src="https://github.com/user-attachments/assets/13ac7d1b-4056-4e64-a10b-7247bb65625c" />

</details> 

ollama ответила

## Поднял второй локальный сервер ollama
OLLAMA_HOST=127.0.0.2:11434 ollama serve

<details>
<summary><b>Смотреть -> второй сервер</b></summary>
<img width="1905" height="903" alt="Снимок экрана от 2026-10-21 15-28-50" src="https://github.com/user-attachments/assets/7d2dcfc3-6965-404d-9381-1477c827e395" />

</details>

- Либо меняем адрес порт стандартный.
- Либо меняем номер порта адрес 127.0.0.1 (порты до 1000 системные).
- Вопрос по памяти (htop, free)? Если 16Гб поднять получится два сервера 

НАПРИМЕР: Чат-бот на втором сервере
OLLAMA_HOST=127.0.0.2:11434 ollama run qwen2.5-coder:7b


