"""
    A splash screen that gives tkinter time to initalize all needed files. 
    For current version, runtime is pre-determined. 
    In future versions, the runtime will be based on each file loading. 
    Window does not fill screen. 
"""

#importing tkinter to open window, * for simplified notation
from tkinter import *

#importing the PIL module to allow for image manipulation (proper sizing)
from PIL import ImageTk, Image

#importing os to allow for user interaction, will be used in future code versions
from os import *

#establishing root branch to be called on for labels and packing, specifies role within splash screen. 
splashRoot = Tk()

#establishes the dimensions of the loading screen, set to match those of the user's device.
splashRoot.overrideredirect(True)

#establishing width and height as vars before manipulating their dimensions throughout the code. 
width = splashRoot.winfo_screenwidth()
height = splashRoot.winfo_screenheight()

#sets geometry so that the window is centered and 1/2 the length of the screen while also being 1/4 the height. 
splashRoot.geometry('%dx%d+%d+%d' % (int(width*0.5), int(height*0.5), int(width*0.25), int(height*0.25)))

#creating image object and converting into a usable form through the PIL module (tkinter --> PIL).
splashImage = Image.open("C:/Users/thema/OneDrive/Senior Internship/GUI/DBBLE_Black.png")

#resizing allows the image to be smaller, and fit entirely in the window provided. LANCZOS for image clarity. 
splashImage = splashImage.resize((int(width*0.5), int(height*0.5)), Image.Resampling.LANCZOS)

#final conversion from tkinter to PIL. 
splashImage = ImageTk.PhotoImage(splashImage)

#establishes a canvas, or host for the image to reside in. Dimensions are stated as original vars, but not modified. 
canvas = Canvas(splashRoot, width=width, height=height, bg="black")

#sets the image's dimensions so that it is centered within the display of the splash screen. 
canvas.create_image(width*0.25, height*0.25, image=splashImage)

#packing the canvas, which includes the values used to define width, height, and the splash image. Should appear in middle of screen. 
canvas.pack()

#setting a timer for the splash screen to dissipate. V1 usage only, once program is written it will lead to opening of app. 
splashRoot.after(5000, splashRoot.destroy)

#calling loop
splashRoot.mainloop()