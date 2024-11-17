#PyCalc V1.0  Date: 09/11/2024 Developer: Lorydima

#Libraries for app Dev.
import math
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label

#Logo Path
logo_path = 'PyCalcV1.0_Logo.ico'

#"Credit" Window Setup
def open_credit_window():
    credit_window = Toplevel(window)
    credit_window.title("Credit")
    credit_window.geometry("300x150")
    credit_window.configure(bg="#1E1E1E")
    credit_window.resizable(False, False)
    credit_window.iconbitmap(logo_path)
    credit_label = Label(credit_window, text="PyCalc Version 1.0\nDeveloper: Lorydima", font=("Arial", 12), bg="#1E1E1E", fg="white")
    credit_label.pack(pady=50)

#Calculator Functions
def button_click(event):
    text = button_texts[event.widget.find_withtag("current")[0]]
    if text == "=":
        try:
            expression = input_var.get().replace("X", "*")
            if "/0" in expression:
                input_var.set("Impossibile")
            else:
                result = str(eval(expression, {"__builtins__": None}, math.__dict__))
                input_var.set(result)
        except Exception:
            input_var.set("Error")
    elif text == "CE":
        input_var.set("")
    elif text == "C":
        input_var.set(input_var.get()[:-1])
    elif text == "Credit":
        open_credit_window()
    else:
        input_var.set(input_var.get() + text)

def key_input(event):
    if event.widget == entry:
        return
    if event.char.isdigit() or event.char in "+-*/":
        input_var.set(input_var.get() + event.char)
    elif event.keysym == "Return":
        try:
            expression = input_var.get().replace("X", "*")
            if "/0" in expression:
                input_var.set("Impossibile")
            else:
                result = str(eval(expression, {"__builtins__": None}, math.__dict__))
                input_var.set(result)
        except Exception:
            input_var.set("Errore")
    elif event.keysym == "BackSpace":
        input_var.set(input_var.get()[:-1])
    elif event.keysym == "Delete":
        input_var.set("")
    elif event.keysym == "Escape":
        window.destroy()

#Window "Calculator" Setup
window = Tk()
window.geometry("327x512")
window.configure(bg="#FFFFFF")
window.title("PyCalc V1.0")

#Windows Logo
window.iconbitmap(logo_path)

#Canvas Setup
canvas = Canvas(
    window,
    bg="#1E1E1E",
    height=512,
    width=327,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

#Input Area
input_var = StringVar()
entry = Entry(window, textvar=input_var, font=("Arial", 20), justify='right', bd=10, bg="#1E1E1E", fg="white")
entry.place(x=10, y=10, width=307, height=60)

#Create white line
canvas.create_rectangle(
    0.0,
    80.0,
    327.0,
    87.95859918062783,
    fill="#FFFFFF",
    outline=""
)

#Calculator Buttons
buttons = [
    ("CE", 17, 115, 78, 168),
    ("C", 91, 115, 152, 168),
    ("Credit", 165, 115, 226, 168),
    ("+", 239, 115, 300, 168),
    ("-", 239, 190, 300, 243),
    ("*", 239, 265, 300, 318),
    ("/", 239, 340, 300, 393),
    ("=", 239, 415, 300, 468),
    ("0", 17, 415, 226, 468),
    ("1", 17, 340, 78, 393),
    ("2", 91, 340, 152, 393),
    ("3", 165, 340, 226, 393),
    ("4", 17, 265, 78, 318),
    ("5", 91, 265, 152, 318),
    ("6", 165, 265, 226, 318),
    ("7", 17, 190, 78, 243),
    ("8", 91, 190, 152, 243),
    ("9", 165, 190, 226, 243)
]
button_texts = {}

for (text, x1, y1, x2, y2) in buttons:
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="#FF0000" if text in "CECCredit+-*/=" else "white", outline="")
    button_texts[rect_id] = text
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill="white" if text in "CECCredit+-*/=" else "black", font=("Arial", 14))
    canvas.tag_bind(rect_id, "<Button-1>", button_click)
    canvas.tag_bind(rect_id, "<Enter>", lambda e: canvas.config(cursor="hand2"))
    canvas.tag_bind(rect_id, "<Leave>", lambda e: canvas.config(cursor=""))

#Window Loop
window.bind("<Key>", key_input)
window.resizable(False, False)
window.mainloop()
