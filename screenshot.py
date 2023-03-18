import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    #time.sleep(5) #timer to take screenshot after 5secs removing it will help us to take screenshot immediately
    img = pyautogui.screenshot(name)
    img.show()


#screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Take Screenshot',
    command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text='QUIT',
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
