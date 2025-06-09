from tkinter import *
from tkinter import ttk, messagebox
import requests


def data_get():
    city = city_name.get()
    if not city:
        messagebox.showerror("Error", "Please select a city")
        return
    try:
        api_key = "7c473e696667017814a458d59286827d"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data = requests.get(url).json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"].capitalize())
            return

        W_label1.config(text=data["weather"][0]["main"], foreground="black")
        Wb_label1.config(text=data["weather"][0]["description"].capitalize(), foreground="black")
        temp_label1.config(text=f"{data['main']['temp'] - 273.15:.2f}°C", foreground="black")
        per_label1.config(text=f"{data['main']['pressure']} hPa", foreground="black")
        humidity_label1.config(text=f"{data['main']['humidity']}%", foreground="black")
        wind_label1.config(text=f"{data['wind']['speed']} m/s", foreground="black")
    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch weather data")


# Main window settings
win = Tk()
win.title("Weather App")
win.geometry("500x650")  # Adjusted height for additional details
win.configure(bg="#f5f5f5")  # Light Grey Background

# Header Label
header_frame = Frame(win, bg="#1976D2", height=80)
header_frame.pack(fill=X)
name_label = Label(header_frame, text="Weather App", font=("Arial", 28, "bold"), bg="#1976D2", fg="white")
name_label.pack(pady=15)

# City Selection
city_name = StringVar()
list_name = (
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Pondicherry", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
)
com = ttk.Combobox(win, values=list_name, font=("Arial", 14), textvariable=city_name, state="readonly", justify=CENTER)
com.pack(pady=20)

# Fetch Weather Button
done_button = Button(win, text="Get Weather", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", relief=FLAT, bd=0,
                     padx=20, pady=10, cursor="hand2", command=data_get)
done_button.pack(pady=10)

# Weather Info Frame
frame = Frame(win, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

labels = ["Weather Climate", "Weather Description", "Temperature", "Pressure", "Humidity", "Wind Speed"]
values = []

for i, label_text in enumerate(labels):
    label = Label(frame, text=label_text, font=("Arial", 16, "bold"), bg="white", fg="#424242", anchor="w")
    label.grid(row=i, column=0, padx=20, pady=10, sticky=W)
    value_label = Label(frame, text="--", font=("Arial", 16), bg="white", fg="#1976D2", anchor="w")
    value_label.grid(row=i, column=1, padx=20, pady=10, sticky=W)
    values.append(value_label)

W_label1, Wb_label1, temp_label1, per_label1, humidity_label1, wind_label1 = values

win.mainloop()
