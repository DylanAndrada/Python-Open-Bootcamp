import tkinter as tk


def handle_radio_selection():
    selected_value = var.get()
    print("Selected:", selected_value)

def handle_button_click():
    var.set("")


window = tk.Tk()

var = tk.StringVar(value="")

radio_button1 = tk.Radiobutton(window, text="Option 1", variable=var, value="Option 1", command=handle_radio_selection)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Option 2", variable=var, value="Option 2", command=handle_radio_selection)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="Option 3", variable=var, value="Option 3", command=handle_radio_selection)
radio_button3.pack()

reset_button = tk.Button(window, text="Reiniciar opciones", command=handle_button_click)
reset_button.pack()

window.mainloop()