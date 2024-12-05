import tkinter as tk
import requests

API_KEY = "02f374cb2312c34383fdd0dbc3dfa75c" 
CITY = "Ульяновск"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"

def get_weather():
    try:
        response = requests.get(URL)
        response.raise_for_status() 
        data = response.json()
        
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]


        weather_info.set(
            f"Город: {city_name}\n"
            f"Температура: {temp}°C\n"
            f"Погода: {weather_desc.capitalize()}\n"
            f"Скорость ветра: {wind_speed} м/с"
        )
    except Exception as e:
        weather_info.set("Не удалось получить данные о погоде.\nПроверьте подключение к Интернету или API-ключ.")


root = tk.Tk()
root.title("Погода в Ульяновске")
root.geometry("300x200")


weather_info = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_info, font=("Arial", 12), justify="left")
weather_label.pack(pady=10)

refresh_button = tk.Button(root, text="Обновить", command=get_weather)
refresh_button.pack(pady=5)

get_weather()

root.mainloop()
