import requests
import time
from datetime import datetime
import random

TOKEN = '7611326711:AAFDeLsblGi1MaJMqAmYQIZRL87RgrQfykQ'
CHAT_ID = '790788313'

# API для пошуку картинок
SEARCH_API_KEY = 'AIzaSyCYzMREOHOaRQZgNxgzXQTnuYVSS3Mcn1U'
CX = '86db45a046f1b4989'

# Рандомні повідомлення
messages = [
    "Сонечко, час хлюпнути водички 💦❤️‍🔥",
    "Гей, гей! Ти ще не пила воду? Ану до склянки! 🥤😼",
    "Крап-крап! Пий воду, а то перетворишся на сухарик 🐪",
    "Вода чекає тебе...",
    "Ти – 70% вода. Підзарядись :3",
    "Давай не цейво, пий водичку щоб бути здоровим котиком (●'◡'●)"
]

# Чорний список використаних картинок
sent_images = set()

# Функція для пошуку унікальної картинки
def get_unique_jimin_image():
    url = f"https://www.googleapis.com/customsearch/v1?q=Jimin BTS&cx={CX}&key={SEARCH_API_KEY}&searchType=image"
    response = requests.get(url).json()

    if 'items' in response:
        random.shuffle(response['items'])  # Перемішуємо картинки
        for item in response['items']:
            image_url = item['link']
            if image_url not in sent_images:
                sent_images.add(image_url)
                return image_url
        return None  # Якщо всі картинки вже були
    else:
        return None

# Функція для надсилання нагадування та картинки
def send_water_reminder():
    now = datetime.now().strftime('%H:%M')
    msg = f"🕒 {now}\n\n" + random.choice(messages)

    # Надсилаємо текстове повідомлення
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"✅ Повідомлення надіслано: {msg}")
        else:
            print(f"❌ Помилка при надсиланні тексту: {response.status_code}")
    except Exception as e:
        print(f"❌ Виняток при надсиланні тексту: {e}")

    # Додаємо унікальну картинку
    image_url = get_unique_jimin_image()
    if image_url:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        payload = {
            "chat_id": CHAT_ID,
            "photo": image_url,
            "caption": "Ось тобі ще одна порція Чіміна на пам'ять! 😍"
        }
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print(f"✅ Картинка надіслана: {image_url}")
            else:
                print(f"❌ Помилка при надсиланні картинки: {response.status_code}")
        except Exception as e:
            print(f"❌ Виняток при надсиланні картинки: {e}")

print("Бот запущено. Нагадування надсилатимуться кожні 40 хвилин з 9:00 до 23:00.")

while True:
    current_hour = datetime.now().hour

    if 9 <= current_hour < 23:  # Перевірка: тільки з 9:00 до 23:00
        send_water_reminder()
        time.sleep(40 * 60)  # 40 хвилин у секундах
    else:
        time.sleep(60)  # Якщо зараз не робочий час — чекати 1 хвилину
