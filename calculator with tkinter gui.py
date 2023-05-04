import tkinter as tk

root = tk.Tk()

root.geometry("300x300")

root.title("calculator")

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)

def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current)+str(num))


def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def clear():
    entry.delete(0, tk.END)

button1 = tk.Button(root, text="1", command= lambda : button_click(1))
button2 = tk.Button(root, text="2", command= lambda : button_click(2))
button3 = tk.Button(root, text="3", command= lambda : button_click(3))
button4 = tk.Button(root, text="4", command= lambda : button_click(4))
button5 = tk.Button(root, text="5", command= lambda : button_click(5))
button6 = tk.Button(root, text="6", command= lambda : button_click(6))
button7 = tk.Button(root, text="7", command= lambda : button_click(7))
button8 = tk.Button(root, text="8", command= lambda : button_click(8))
button9 = tk.Button(root, text="9", command= lambda : button_click(9))
button0 = tk.Button(root, text="0", command= lambda : button_click(0))

button_add = tk.Button(root, text="+", command= lambda: button_click("+"))
button_sub = tk.Button(root, text="-", command= lambda : button_click("-"))
button_mul = tk.Button(root, text="*", command= lambda : button_click("*"))
button_div = tk.Button(root, text="/", command= lambda : button_click("/"))
button_equal = tk.Button(root, text="=", command= calculate)
button_clear = tk.Button(root, text="C", command= clear)

button_name = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button0, button_add, button_sub, button_mul,button_div,button_equal]

for i in range(len(button_name)):
    if i < 11:
        button_name[i].grid(row=int(i/3)+1, column=i%3)
    elif i == 11:
        button_name[i].grid(row=1, column=3)
    elif i == 12:
        button_name[i].grid(row=2, column=3)
    elif i == 13:
        button_name[i].grid(row=3, column=3)
    else:
        button_name[i].grid(row=4, column=i%3)

button_clear.grid(row=4, column=3, sticky="nsew")

root.mainloop()
