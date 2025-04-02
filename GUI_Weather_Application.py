import tkinter
from tkinter import PhotoImage
from tkinter import ttk
import requests
import json

def func_get_weather():
    city=select_city_dropdown.get()
    api_key="7b9190d406412f4f3fe3bba43057d3fe"
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    server_data=requests.get(api_url)
    server_data_json=server_data.json()
    temp=server_data_json["main"]["temp"]
    feels=server_data_json["main"]["feels_like"]
    temp_min=server_data_json["main"]["temp_min"]
    temp_max=server_data_json["main"]["temp_max"]
    pressure=server_data_json["main"]["pressure"]
    humidity=server_data_json["main"]["humidity"]
    output_label.config(text=f'Temperature: {temp} C\n'
                             f'Feels_Like: {feels}\n'
                             f'Temp_Min: {temp_min}\n'
                             f'Temp_Max: {temp_max}\n'
                             f'Pressure: {pressure}\n'
                             f'Humidity: {humidity}%'
                        
                        )
    output_frame.pack()

root=tkinter.Tk()
root.geometry("500x600")
root.title("My Weather App")

image_path=r"C:\Users\abhis\Desktop\Python_File\pxfuel.png"
bg_image=PhotoImage(file=image_path)
set_bg_image=tkinter.Label(root,image=bg_image)
set_bg_image.place(relheight=1,relwidth=1)

app_header=tkinter.Label(root,text="My Weather App", font=("Georgia",24), bg="White",fg="Black",highlightbackground="Blue",highlightthickness=5,)
app_header.pack(pady=20)

select_city_label=tkinter.Label(root,text="Select City", font=("Georgia",15))
select_city_label.pack(pady=20)

cities=["Bengaluru","Mumbai","Kolkata","Pune","Goa","Delhi"]
select_city_dropdown=ttk.Combobox(root,values=cities,font=("Georgia",10))
select_city_dropdown.pack(pady=20)

get_weather_button=tkinter.Button(root,text="Get Weather",font=("Georgia",15),command=func_get_weather)
get_weather_button.pack(pady=10)

output_frame=tkinter.Frame(root,highlightbackground="Blue",highlightthickness=5)

output_label=tkinter.Label(output_frame,text="",font=("Georgia",15))
output_label.pack(pady=10)

root.mainloop()