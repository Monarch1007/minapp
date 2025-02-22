from tkinter import *
from PIL import Image, ImageTk  # Import Pillow to handle images
import requests

# Initialize main window
root = Tk()
root.title("Weather App")
root.geometry("550x350+500+200")  # Increased height for better layout
root.resizable(False, False)
icon=PhotoImage(file="1.png") 
root.iconphoto(False,icon)

# Load and set background image
bg_image = Image.open("background.jpg")  # Ensure image is in the same directory
bg_image = bg_image.resize((550, 350), Image.LANCZOS)  # Resize to fit window
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover entire window

# Title Label
title_label = Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#292929", fg="white")
title_label.place(x=180, y=10)

# Location Label & Entry
location_label = Label(root, text="Enter City:", font=("Arial", 12), bg="#292929", fg="white")
location_label.place(x=50, y=60)

location_entry = Entry(root, font=("Arial", 14), bd=2, relief=GROOVE, justify="center", width=20)
location_entry.place(x=150, y=60)

# Function to fetch weather data
def get_weather():
    city_name = location_entry.get()
    API_key = "401ecca7dcbe0686e714ef2a8de05a2e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        Condition = data["weather"][0]["description"].capitalize()
        temp = str(data["main"]["temp"])
        humidity = str(data["main"]["humidity"])

        text_ = f"🌡 Temperature: {temp}°C\n🌥 Condition: {Condition}\n💧 Humidity: {humidity}%"

        # Update label dynamically
        weather_data.config(text=text_, bg="#FFFFFF", fg="#333333")
    else:
        weather_data.config(text="❌ City not found!", bg="red", fg="white")

# Get Weather Button
get_weather_button = Button(root, text="Get Weather", command=get_weather, font=("Arial", 12, "bold"), bg="orange", fg="white", bd=3, relief=RAISED, padx=10, pady=5)
get_weather_button.place(x=200, y=100)

# Weather Info Frame
weather_frame = LabelFrame(root, text="Weather Info", font=("Arial", 12, "bold"), bg="white", fg="#333333", bd=3, relief=GROOVE, padx=10, pady=10)
weather_frame.place(x=50, y=160, width=450, height=120)

# Weather Data Label
weather_data = Label(weather_frame, text="🌡 Temperature: --°C\n🌥 Condition: --", font=("Arial", 12), bg="white", fg="#333333", justify="left")
weather_data.pack(padx=10, pady=10)

# Run the application
root.mainloop()
