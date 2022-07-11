from tkinter import *
window=Tk()

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)

window.title('Hello Python')
window.geometry("300x200+10+10")

window.mainloop()
