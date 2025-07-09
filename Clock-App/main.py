import tkinter as tk
import time
import math
# Creating a window
window = tk.Tk()
window.title("Clock-App")
window.config(
    width=400,
    height=300,
    bg="black",
    padx=20,
    pady=50
)
window.resizable(True, True)

# Clock text
clock_text = tk.Label(
    window, 
    text="Clock", 
    font=("Arial", 25),
    fg="white",
    bg="black",
    padx=100,
    pady=10,
)
clock_text.place(x=130, y=20)
clock_text.pack(expand=True)

# the clock
clock = tk.Label(
    font=("Arial", 35),
    fg="white",
    bg="black"

)
clock.place(x=110, y=100)
clock.pack(expand=True)

def update_time():
    formatted_time = time.strftime("%H:%M:%S")
    clock.config(text=formatted_time)
    window.after(1000,update_time)
    pass

update_time()
window.mainloop()
