import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    # OpenWeatherMap API URL
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":  # If city found
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]

            # Display the weather info in the labels
            temperature_label.config(text=f"Temperature: {temperature}°C")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            humidity_label.config(text=f"Humidity: {humidity}%")
            description_label.config(text=f"Description: {description.capitalize()}")
        else:
            messagebox.showerror("City Not Found", "City not found, please try again.")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch weather data. Please check your internet connection.")

# Setting up the GUI window
root = tk.Tk()
root.title("Weather Application")
root.geometry("400x300")

# Label and Entry for city input
city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 14))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

# Button to get weather
get_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
get_button.pack(pady=10)

# Labels to display weather information
temperature_label = tk.Label(root, text="Temperature: --°C", font=("Arial", 12))
temperature_label.pack(pady=5)

pressure_label = tk.Label(root, text="Pressure: -- hPa", font=("Arial", 12))
pressure_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: --%", font=("Arial", 12))
humidity_label.pack(pady=5)

description_label = tk.Label(root, text="Description: --", font=("Arial", 12))
description_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
