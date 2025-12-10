import sys
import os
from urllib.parse import urlparse

import dns.resolver
from dotenv import load_dotenv

load_dotenv()

def get_domain(email: str) -> str:
    if "@" not in email:
        return ""
    return email.rsplit("@", 1)[1].strip().lower()


def check_domain(domain: str) -> str:
    if not domain:
        return "домен отсутствует"
    try:
        # попытка получить MX записи
        answers = dns.resolver.resolve(domain, 'MX', lifetime=5)
        mx_records = [r.exchange.to_text() for r in answers]
        if mx_records:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except dns.resolver.NoAnswer:
        return "MX-записи отсутствуют или некорректны"
    except dns.resolver.Timeout:
        return "MX-записи отсутствуют или некорректны"
    except Exception as e:
        return "MX-записи отсутствуют или некорректны"


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_mx.py emails.txt")
        sys.exit(1)
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Файл не найден: {path}")
        sys.exit(2)

    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]

    for email in lines:
        domain = get_domain(email)
        status = check_domain(domain)
        print(f"{email}\t-> {status}")


if __name__ == '__main__':
    main()
