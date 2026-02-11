import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import pygame
import time
from datetime import datetime, date
# -------------------------------
# 1) USER DETAILS (CHANGE THIS)
# -------------------------------
# Simplified Chandra Rashi logic (DOB only)
USER_DOB = datetime(1998, 7, 15)   # YYYY, MM, DD

# -------------------------------
# 2) CHANDRA RASHI CALCULATION (SIMPLIFIED)
# -------------------------------
def get_chandra_rashi(dob):
    month = dob.month
    day = dob.day

    # Simplified moon-sign ranges (approximate)
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "mesh"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "vrushabh"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "mithun"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "kark"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "singh"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "kanya"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "tula"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "vrushchik"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "dhanu"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "makar"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "kumbh"
    else:
        return "meen"

rashi = get_chandra_rashi(USER_DOB)

# -------------------------------
# 3) RASHI → URL MAP
# -------------------------------
RASHI_URLS = {
    "mesh": "https://www.divyabhaskar.co.in/rashifal/13/today",
    "vrushabh": "https://www.divyabhaskar.co.in/rashifal/14/today",
    "mithun": "https://www.divyabhaskar.co.in/rashifal/15/today",
    "kark": "https://www.divyabhaskar.co.in/rashifal/16/today",
    "singh": "https://www.divyabhaskar.co.in/rashifal/17/today",
    "kanya": "https://www.divyabhaskar.co.in/rashifal/18/today",
    "tula": "https://www.divyabhaskar.co.in/rashifal/19/today",
    "vrushchik": "https://www.divyabhaskar.co.in/rashifal/20/today",
    "dhanu": "https://www.divyabhaskar.co.in/rashifal/21/today",
    "makar": "https://www.divyabhaskar.co.in/rashifal/22/today",
    "kumbh": "https://www.divyabhaskar.co.in/rashifal/23/today",
    "meen": "https://www.divyabhaskar.co.in/rashifal/24/today",
}

url = RASHI_URLS[rashi]

# -------------------------------
# 8) RUN ONCE PER DAY (AFTER 5 MINUTES)
# -------------------------------
STATE_FILE = "last_played.txt"
today = date.today().isoformat()

if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        if f.read() == today:
            print("Rashi bhavishya already played today.")
            exit()

print("Waiting 5 minutes after laptop start...")
time.sleep(300)  # 5 minutes

# -------------------------------
# 4) FETCH DATA
# -------------------------------
try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # -------------------------------
        # 5) EXTRACT DATA
        # -------------------------------
        content = soup.find("div", class_="a6b3d8fe")
        text = content.text.strip()

        # -------------------------------
        # 6) TEXT TO SPEECH
        # -------------------------------
        tts = gTTS(text=text, lang="gu", slow=False)
        audio_file = "rashi.mp3"
        tts.save(audio_file)

        # -------------------------------
        # 7) PLAY SOUND
        # -------------------------------
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        # Save today's date
        with open(STATE_FILE, "w") as f:
            f.write(today)

        print("Rashi bhavishya played successfully.")

    else:
        print("Failed to fetch horoscope")

except Exception as e:
    print("Error:", e)

