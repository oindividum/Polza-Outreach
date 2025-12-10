
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

API_URL = 'https://api.telegram.org'


def send_text(chat_id: str, text: str) -> dict:
    if not TELEGRAM_BOT_TOKEN or not chat_id:
        raise RuntimeError('TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID должны быть заданы в окружении')
    url = f"{API_URL}/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    r = requests.post(url, data=payload, timeout=10)
    r.raise_for_status()
    return r.json()


def main():
    if len(sys.argv) < 2:
        print('Usage: python tg_send.py message.txt')
        sys.exit(1)
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f'File not found: {path}')
        sys.exit(2)

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    try:
        resp = send_text(TELEGRAM_CHAT_ID, text)
        print('Sent. message_id=', resp.get('result', {}).get('message_id'))
    except Exception as e:
        print('Error sending message:', e)
        sys.exit(3)


if __name__ == '__main__':
    main()