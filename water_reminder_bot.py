import requests
import time
from datetime import datetime

TOKEN = '7611326711:AAFDeLsblGi1MaJMqAmYQIZRL87RgrQfykQ'
CHAT_ID = '790788313'  # Наприклад: '123456789'

messages = [
    "Сонечко, час хлюпнути водички 💦❤️‍🔥",
    "Гей, гей! Ти ще не пила воду? Ану до склянки! 🥤😼",
    "Крап-крап! Пий воду, а то перетворишся на сухарик 🐪",
    "Вода чекає тебе...",
    "Ти – 70% вода. Підзарядись :3",
    "Давай не цейво, пий водичку щоб бути здоровим котиком (●'◡'●)"
]

def send_water_reminder():
    now = datetime.now().strftime('%H:%M')
    msg = f"🕒 {now}\n\n" + messages[int(time.time()) % len(messages)]
    
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
            print(f"❌ Помилка: {response.status_code}")
    except Exception as e:
        print(f"❌ Виняток: {e}")

print("Бот запущено. Нагадування надсилатимуться кожні 40 хвилин в період з 9:00 до 23:00.")

while True:
    current_hour = datetime.now().hour
    
    if 9 <= current_hour < 23:  # Перевірка, чи в межах 9:00 - 23:00
        send_water_reminder()
        time.sleep(40 * 60)  # 40 хвилин
    else:
        time.sleep(60)  # Перевірка кожну хвилину, якщо бот не працює
