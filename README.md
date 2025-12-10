#  Polza Outreach — Тестовое задание

**Проверка MX-записей доменов и отправка текста в приватный Telegram-чат**

Проект включает два небольших, но полноценных инструмента:

-  **Проверка доменов email по MX-записям**
-  **Отправка текста из файла в Telegram-чат через Telegram Bot API**

---

##  Структура проекта

```
polza-outreach-test/
│
├── check_mx.py          # Проверка MX-записей email-доменов
├── tg_send.py           # Отправка текста в Telegram
├── requirements.txt      # Зависимости проекта
├── .env.example         # Пример файла окружения
├── architecture.md      # Архитектурное предложение
├── README.md            # (этот файл)
│
├── emails.txt           # Пример входных email
└── message.txt          # Пример сообщения для Telegram
```

---

##  Установка и запуск

### 1. Создайте виртуальное окружение
```bash
python -m venv venv
```

### 2. Активируйте окружение
**Windows:**
```bash
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

---

##  Настройка окружения

Создайте файл `.env` по образцу `.env.example`:

```
TELEGRAM_BOT_TOKEN=ваш_бот_токен
TELEGRAM_CHAT_ID=целевой_chat_id
```

> ** Важно:** Реальные токены не загружаются в GitHub!

---

##  Проверка MX-записей

Скрипт `check_mx.py` принимает файл со списком email-ов и выводит статус каждого домена.

### Пример входного файла (`emails.txt`)
```
test@gmail.com
info@yandex.ru
example@nonexistentdomain123321.com
```

###  Запуск:
```bash
python check_mx.py emails.txt
```

###  Пример вывода:
```
test@gmail.com                      -> домен валиден
info@yandex.ru                      -> домен валиден
example@nfkjnekfjkk123432.com-> домен отсутствует
```

---

##Отправка сообщений в Telegram

Скрипт `tg_send.py` отправляет текст из файла в указанный приватный Telegram-чат.

### Пример входного файла (`message.txt`)
```
Привет это тестовое сообщение, отправленное через Telegram-бота.
```

### Запуск:
```bash
python tg_send.py message.txt
```

### Пример успешного ответа:
```
Sent. message_id=1049
```

---

## Как узнать `chat_id` Telegram-чата

1. **Добавьте бота в чат**
2. **Напишите любое сообщение**
3. **Откройте в браузере:**
   ```
   https://api.telegram.org/bot<ВАШ_ТОКЕН>/getUpdates
   ```
4. **В ответе будет:**
   ```json
   "chat": {
     "id": -1001234567890,
     "title": "Название чата"
   }
   ```

---

## Архитектура решения

Подробно описана в файле `architecture.md`.

**Главные идеи:**
- Очередь задач + serverless-воркеры
- Ротация SMTP-провайдеров
- Минимальная стоимость
- Автоматический health-check отправки

---

##  Требования
```
dnspython>=2.0.0
python-dotenv>=0.21.0
requests>=2.28.0
```

---

