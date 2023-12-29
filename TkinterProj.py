import tkinter as tk
from tkinter import Label, Listbox, Button
import matplotlib.pyplot as plt

# Функція для розрахунку часу роботи алгоритму
def calculate_time(n):
    f = []
    for i in n:
        f.append(i * 2 * 10**-6)
    return f

# Функція для побудови графіка
def btn1_cl():
    plt.title("Час роботи, с")
    plt.xlabel('n', color='gray')
    plt.plot(n, calculate_time(n))
    plt.ylabel('f', color='gray')
    plt.show()

# Створення головного вікна програми
root = tk.Tk()
root.title("Час роботи")

# Список значень кількості вхідних даних
n = [10, 100, 200, 300, 400, 500]

# Віджет Label для "Кількість даних"
lab1 = Label(text="Кількість даних")
lab1.grid(row=0, column=0)

# Віджет Listbox для вибору кількості даних
box1 = Listbox(root)
box1.grid(row=1, column=0, rowspan=6)
for p in n:
    box1.insert(tk.END, p)

# Віджет Label і Listbox для відображення часу роботи
lab2 = Label(text="Час роботи")
lab2.grid(row=0, column=1)
box2 = Listbox(root)
box2.grid(row=1, column=1, rowspan=6)

# Віджет Button для виклику функції побудови графіка
btn1 = Button(text="Графік", command=btn1_cl)
btn1.grid(row=2, column=2)

# Запуск головного циклу подій
tk.mainloop()
