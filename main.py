import requests
import os

def telegram_bot_send_text(bot_message):

    bot_token = os.environ.get("BOT_TOKEN")
    bot_chatID = os.environ.get("BOT_CHATID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


api_key = os.environ.get("OWM_API_KEY")
lat = os.environ.get("LAT")
lon = os.environ.get("LON")

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

is_rain = False
for hour_data in data["list"]:
    for weather in hour_data["weather"]:
        print(weather["id"])
        if weather["id"] < 700:
            test = telegram_bot_send_text("Bring an umbrella.")
            is_rain = True
            break
    if is_rain:
        break
