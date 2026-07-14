import tkinter as tk 
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

entry = tk.Entry(window, width=20,font=("Arial", 20)) 
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(number):
    entry.insert(tk.END, number)
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 

button7 = tk.Button(window, text="7",width=5, height=2, command=lambda: click(7))
button7.grid(row=1, column=0, padx=5, pady=5) 

button8 = tk.Button(window, text="8",width=5, height=2, command=lambda: click(8))
button8.grid(row=1, column=1, padx=5, pady=5)

button9 = tk.Button(window, text="9",width=5, height=2, command=lambda: click(9))
button9.grid(row=1, column=2, padx=5, pady=5)

button6 = tk.Button(window, text="6",width=5, height=2, command=lambda: click(6))
button6.grid(row=2, column=2, padx=5, pady=5)

button5 = tk.Button(window, text="5",width=5, height=2, command=lambda: click(5))
button5.grid(row=2, column=1, padx=5, pady=5)

button4 = tk.Button(window, text="4",width=5, height=2, command=lambda: click(4))
button4.grid(row=2, column=0, padx=5, pady=5)

button3 = tk.Button(window, text="3",width=5, height=2, command=lambda: click(3))
button3.grid(row=3, column=2, padx=5, pady=5)

button2 = tk.Button(window, text="2",width=5, height=2, command=lambda: click(2))
button2.grid(row=3, column=1, padx=5, pady=5)

button1 = tk.Button(window, text="1",width=5, height=2, command=lambda: click(1))
button1.grid(row=3, column=0, padx=5, pady=5)

button0 = tk.Button(window, text="0",width=5, height=2, command=lambda: click(0))
button0.grid(row=4, column=1, padx=5, pady=5)

button_divide = tk.Button(window, text="/",width=5, height=2, command=lambda: click("/"))
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_multiply = tk.Button(window, text="*",width=5, height=2, command=lambda: click("*"))
button_multiply.grid(row=2, column=3, padx=5, pady=5)

button_subtract = tk.Button(window, text="-",width=5, height=2, command=lambda: click("-"))
button_subtract.grid(row=4, column=3, padx=5, pady=5)

button_add = tk.Button(window, text="+",width=5, height=2, command=lambda: click("+"))
button_add.grid(row=3, column=3, padx=5, pady=5)

button_percentage = tk.Button(window, text="%",width=5, height=2, command=lambda: click("%"))
button_percentage.grid(row=4, column=2, padx=5, pady=5)

clear_button =  tk.Button(window, text="Clear", width=10, height=2, command=clear)
clear_button.grid(row=4, column=0, padx=5, pady=5)

equal_button =  tk.Button(window, text="=", width=10, height=2, command=calculate)
equal_button.grid(row=4, column=3, padx=5, pady=5)


window.mainloop()