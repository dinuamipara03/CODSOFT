import tkinter as tk
from tkinter import messagebox
import requests


def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = "e4a9422d09f27897c1f07bd8fff59de1"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
        }
        return weather_info
    else:
        return None


def display_weather(city):
    weather_info = get_weather(city)

    if weather_info:
        message = (
            f"Temperature: {weather_info['temperature']}°C\n"
            f"Humidity: {weather_info['humidity']}%\n"
            f"Wind Speed: {weather_info['wind_speed']} m/s\n"
            f"Description: {weather_info['description']}"
        )
        messagebox.showinfo("Weather Forecast", message)
    else:
        messagebox.showerror("Error", "Unable to retrieve weather information.")


def show_weather():
    city = city_entry.get()
    display_weather(city)


# Create the main window
root = tk.Tk()
root.title("Weather Forecast")

# Create and place widgets
city_label = tk.Label(root, text="Enter city name or zip code:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

weather_button = tk.Button(root, text="Get Weather", command=show_weather)
weather_button.pack(pady=5)

# Center the main window on the screen
window_width = 250
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 3.5)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Run the GUI
root.mainloop()
