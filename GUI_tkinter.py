from tkinter import * 
from tkinter import ttk 
import time
from main import *

from PIL import Image, ImageTk

BLACK = '#000000'
WHITE = '#FFFFFF'
FONT = ('Regular',13)


window = Tk()

window.title('GPS')
window.minsize(width=320,height=480)
window.maxsize(width=320,height=480)

window.geometry("320x480")
window.config(background=BLACK)


#First row 
image_sats = Image.open('images/satellite.png')
image_sats = ImageTk.PhotoImage(image_sats)
label_image_sats = Label(window, image=image_sats,background=BLACK)
label_image_sats.grid(row=0, column=0)
label_sats = Label(window, text="00",fg=WHITE,background=BLACK,font=FONT)
label_sats.grid(row=0, column=1)

ttk.Separator(window, orient=VERTICAL).grid(column=2, row=0, rowspan=1, sticky='ns', padx=8)

label_pressure = Label(window, text="0000 hPa",fg=WHITE,background=BLACK,font=FONT)
label_pressure.grid(row=0, column=3)

ttk.Separator(window, orient=VERTICAL).grid(column=4, row=0, rowspan=1, sticky='ns', padx=8)

label_time = Label(window, text="00:00:00",fg=WHITE,background=BLACK,font=FONT)
label_time.grid(row=0, column=5)

ttk.Separator(window, orient=VERTICAL).grid(column=6, row=0, rowspan=1, sticky='ns', padx=8)

label_batterie= Label(window, text="00%",fg=WHITE,background=BLACK,font=FONT)
label_batterie.grid(row=0, column=8)
image_batterie = Image.open('images/batterie.png')
image_batterie = ImageTk.PhotoImage(image_batterie)
label_image_batterie = Label(window, image=image_batterie,background=BLACK)
label_image_batterie.grid(row=0, column=9)

#Second row







#Third row
label_alt_text = Label(window, text="ALT",fg=WHITE,background=BLACK,font=FONT)
label_alt_text.grid(row=1, column=0,columnspan=3)
label_alt = Label(window, text="0000 m",fg=WHITE,background=BLACK,font=FONT)
label_alt.grid(row=2, column=0,columnspan=3)



label_therm_text = Label(window, text="THERM.",fg=WHITE,background=BLACK,font=FONT)
label_therm_text.grid(row=1, column=2,columnspan=3)
label_therm = Label(window, text="00 m/s",fg=WHITE,background=BLACK,font=FONT)
label_therm.grid(row=2, column=2,columnspan=3)



label_speed_text = Label(window, text="SPEED",fg=WHITE,background=BLACK,font=FONT)
label_speed_text.grid(row=1, column=4,columnspan=2)
label_speed = Label(window, text="000 km/h",fg=WHITE,background=BLACK,font=FONT)
label_speed.grid(row=2, column=4,columnspan=2)

image_settings = PhotoImage(file="images/settings.png")
settings_button = Button(window,image=image_settings,bg=BLACK)
settings_button.grid(row=2, column=7,columnspan=2)



data = data()

def update_sat():
    sats = data['sat']
    label_sats.config(text=sats)
    window.after(1000,update_sat)

def update_press():
    press = data['localQNH']
    label_pressure.config(text=press)
    window.after(1000,update_press)


def update_bat():
    #TODO
    pass

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label_time.config(text=current_time)
    window.after(1000,update_time)

def update_alt():
    alt = data['alt']
    label_alt.config(text=alt)
    window.after(1000,update_alt)

def update_therm():
    therm = vertical_speed(data['alt'])
    label_therm.config(text=therm)
    window.after(1,update_therm)

def update_speed():
    speed = data['speed']
    label_speed.config(text=speed)
    window.after(1000,update_therm)

def update_alt():
    alt = data['alt']
    label_alt.config(text=alt)
    window.after(1000,update_alt)

update_sat()
update_press()    
update_time()
update_alt()
update_therm()
update_speed()


window.mainloop()
