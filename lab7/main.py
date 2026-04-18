from tkinter import ttk, messagebox
import tkinter as tk
from mypackage.vehicles import PassengerCar, Truck, Bus
from mypackage.database import save_to_db, get_history
from mypackage.report import save_to_excel

root = tk.Tk() #созд окна
root.title("Калькулятор расхода топлива") #подпись окна
root.geometry("400x400") #размер окна

title=tk.Label(root,text="Расчёт расхода топлива", font=("Arial", 16, "bold")) #метка 
title.pack(pady=10) #отступ 

tk.Label(root, text="Тип автомобиля:").pack() #метка 
car_combo = ttk.Combobox(root, values=["Легковой", "Грузовой", "Пассажирский"]) #список
car_combo.set("Легковой")  # значение по умолчанию
car_combo.pack(pady=5) # размещение в окне

loaded_var=tk.BooleanVar()
tk.Checkbutton(root, text="Груженый", variable=loaded_var).pack(pady=5)

tk.Label(root,text="Расстояние (км):").pack(pady=5)
distance_entry = tk.Entry(root)
distance_entry.pack(pady=5)

time_result = tk.Label(root, text="", fg="blue")
time_result.pack(pady=5)
fuel_result = tk.Label(root, text="", fg="green")
fuel_result.pack(pady=5)

def calculate_time():
    try:
        distance = float(distance_entry.get())
        car_type = car_combo.get()
        is_loaded = loaded_var.get()
        if car_type == "Легковой":car = PassengerCar("Легковой", 80, 8, 4)
        elif car_type == "Грузовой":car = Truck("Грузовой", 60, 15)
        else:car = Bus("Пассажирский", 70, 12)
        speed = car.get_speed(is_loaded)
        time_hours = distance / speed
        hours = int(time_hours) # Переводим часы в часы и минуты
        minutes = int((time_hours - hours) * 60)
        result = f" Время: {hours} ч {minutes} мин"
        time_result.config(text=result, fg="blue")
    except ValueError:
        time_result.config(text="Введите число!", fg="red")

def calculate_fuel():
    try:
        distance = float(distance_entry.get())
        car_type = car_combo.get()
        is_loaded = loaded_var.get()
        if car_type == "Легковой":car = PassengerCar("Легковой", 80, 8, 4)
        elif car_type == "Грузовой":car = Truck("Грузовой", 60, 15)
        else:car = Bus("Пассажирский", 70, 12)
        consumption = car.get_consumption(is_loaded)
        fuel_liters = (distance / 100) * consumption #Рассчет литров
        total_cost = fuel_liters * 55 #Рассчет стоимости
        result = f" {fuel_liters:.1f} л | {total_cost:.0f} руб"
        fuel_result.config(text=result, fg="green")
    except ValueError:
        fuel_result.config(text="Введите число!", fg="red")
tk.Button(root, text="Рассчитать время",command=calculate_time , bg="lightblue").pack(pady=5)
tk.Button(root, text="Рассчитать топливо",command=calculate_fuel , bg="lightgreen").pack(pady=5)       
def show_history():
    rows = get_history() # Получаем все записи из базы данных
    if rows: # Если список не пустой
        text = "ИСТОРИЯ:\n\n" # Заголовок
        for r in rows[-10:]:  # последние 10 записей
            text += f"{r[0]}: {r[1]} км | {r[2]} | "
            text += f"{'Груз' if r[3] else 'Пусто'} | {r[4]}: {r[5]}\n"
        messagebox.showinfo("История", text)
    else:
        messagebox.showinfo("История", "Нет расчетов")

def save_report():
    rows = get_history()
    if rows:
        save_to_excel(rows, "report.xlsx")
        messagebox.showinfo("Сохранено", "Отчет сохранен в report.xlsx")
    else:
        messagebox.showwarning("Нет данных", "Нет расчетов для сохранения")

tk.Button(root, text="История расчетов", command=show_history).pack(pady=5)
tk.Button(root, text="Сохранить в Excel", command=save_report).pack(pady=5)
root.mainloop()