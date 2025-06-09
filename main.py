from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7c473e696667017814a458d59286827d").json()

    W_label1.config(text=data["weather"][0]["main"])
    Wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg = "blue")
win.geometry("500x570")

name_label = Label(win, text=" Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = (
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Pondicherry", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
)

com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text=" Weather Climate", font=("Time New Roman", 16))
W_label.place(x=25, y=260, height=50, width=210)

W_label1 = Label(win, text="", font=("Time New Roman", 16))
W_label1.place(x=250, y=260, height=50, width=210)

Wb_label = Label(win, text=" Weather Description", font=("Time New Roman", 16))
Wb_label.place(x=25, y=330, height=50, width=210)

Wb_label1 = Label(win, text="", font=("Time New Roman", 16))
Wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Time New Roman", 17))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 17))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Time New Roman", 17))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Time New Roman", 17))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("Time New Roman", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
