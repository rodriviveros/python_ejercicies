import tkinter as tk
window=tk.Tk()
window.title("Mi primera APP")
window.geometry("400x300")
Ibl_mensaje=tk.Label(window,text="Hola Mundo!",font=("Arial",24,"bold")) 
Ibl_mensaje.pack(pady=10)
window.mainloop()