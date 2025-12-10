## Содержимое
- `check_mx.py` — проверка MX-записей доменов по списку email.
- `tg_send.py` — отправка текста из `.txt` в приватный Telegram-чат.
- `requirements.txt`, `.env.example`.
- `architecture.md` — архитектурное предложение на 0.5–1 страницу.

## Быстрый старт
1. Склонируй / скачай репо.
2. Создай виртуальное окружение:
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows (PowerShell)
venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
