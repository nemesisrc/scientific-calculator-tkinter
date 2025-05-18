import tkinter as tk
import os
from dotenv import load_dotenv
load_dotenv()


#setting up the main application window
window = tk.Tk()
window.title("Scientific Calculator v1.0")
window.geometry("400x600")
window.configure(bg="#2E2E2E")
window.resizable(True, True)  #x-axis and y-axis 
window.overrideredirect(False)  #removes the title bar

#run the main application
window.mainloop()

