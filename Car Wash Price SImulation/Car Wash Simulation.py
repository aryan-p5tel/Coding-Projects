import tkinter as tk
from tkinter import ttk

# --- Window setup ---
window = tk.Tk()
window.title("Car Wash Simulation")
window.geometry("600x750")
window.configure(background="lightgrey")
window.resizable(False, False)

# --- Variables ---
total_price = 0
tip_price = 0
final_clicked = False

vehicle_choice = tk.StringVar(value="Bike")
service_choice = tk.StringVar(value="Exterior")
extras_vars = {"Waxing": tk.IntVar(), "Drying": tk.IntVar(), "Polishing": tk.IntVar()}
currency = tk.StringVar(value="GBP")

currency_rates = {"GBP": 1, "EUR": 1.14, "USD": 1.25}
currency_symbols = {"GBP": "£", "EUR": "€", "USD": "$"}

# --- Functions ---
def recalc_total():
    global total_price
    base_prices = {"Bike":10, "Car":16, "Truck":40}
    service_prices = {"Exterior":0, "Interior+Exterior":5, "Premium":20}
    extras_prices = {"Waxing":5, "Drying":3, "Polishing":10}

    subtotal_gbp = base_prices.get(vehicle_choice.get(),0)
    subtotal_gbp += service_prices.get(service_choice.get(),0)
    subtotal_gbp += sum(price for var, price in extras_prices.items() if extras_vars[var].get())

    subtotal_converted = round(subtotal_gbp * currency_rates[currency.get()], 2)
    total_price = subtotal_converted + tip_price
    label_total.config(text=f"{currency.get()} {total_price:.2f}")
    label_tip.config(text=f"Tip {currency_symbols[currency.get()]}1")

def add_tip():
    global tip_price
    tip_price += 1  # Always 1 unit of current currency
    if final_clicked:
        recalc_total()

def subtract_tip():
    global tip_price
    tip_price -= 1
    if tip_price < 0:
        tip_price = 0
    if final_clicked:
        recalc_total()

def final_price():
    global final_clicked
    final_clicked = True
    recalc_total()

def on_option_change(*args):
    if final_clicked:
        recalc_total()

# --- Widgets ---
# Title
label_main = tk.Label(window, text="Welcome to the Car Wash Simulation",
                      fg="black", bg="#B8B8B8", font=("Arial", 18, "bold"), padx=10, pady=10)
label_main.grid(row=0, column=0, columnspan=3, pady=20)

# Currency selector
tk.Label(window, text="Currency:", bg="lightgrey", font=("Arial",12)).grid(row=1, column=0, sticky="w", padx=20)
currency_menu = ttk.OptionMenu(window, currency, currency.get(), "GBP", "EUR", "USD", command=lambda e: on_option_change())
currency_menu.grid(row=1, column=1, sticky="w")
currency.trace("w", on_option_change)

# Vehicle selection
tk.Label(window, text="Select type of vehicle:", bg="white", font=("Arial",14)).grid(row=2, column=0, sticky="w", padx=20, pady=(15,5))
vehicle_menu = ttk.OptionMenu(window, vehicle_choice, vehicle_choice.get(), "Bike", "Car", "Truck", command=lambda e: on_option_change())
vehicle_menu.grid(row=3, column=0, sticky="w", padx=50)

# Service selection
tk.Label(window, text="Select type of service:", bg="white", font=("Arial",14)).grid(row=4, column=0, sticky="w", padx=20, pady=(15,5))
service_menu = ttk.OptionMenu(window, service_choice, service_choice.get(), "Exterior", "Interior+Exterior", "Premium", command=lambda e: on_option_change())
service_menu.grid(row=5, column=0, sticky="w", padx=50)

# Extras selection
tk.Label(window, text="Extras:", bg="white", font=("Arial",14)).grid(row=6, column=0, sticky="w", padx=20, pady=(15,5))
row_index = 7
for extra, var in extras_vars.items():
    tk.Checkbutton(window, text=f"{extra} - {currency_symbols[currency.get()]}{5 if extra=='Waxing' else 3 if extra=='Drying' else 10}",
                   variable=var, bg="lightgrey", font=("Arial",12),
                   command=on_option_change).grid(row=row_index, column=0, sticky="w", padx=50)
    row_index += 1

# Tip controls
label_tip = tk.Label(window, text=f"Tip {currency_symbols[currency.get()]}1", bg="lightgrey", font=("Arial",12))
label_tip.grid(row=row_index, column=0, sticky="w", padx=20, pady=(15,5))

btn_plus = tk.Button(window, text="+", command=add_tip, bg="green", font=("Arial",14), width=4)
btn_minus = tk.Button(window, text="-", command=subtract_tip, bg="red", font=("Arial",14), width=4)
btn_plus.grid(row=row_index, column=1, sticky="w", padx=5)
btn_minus.grid(row=row_index, column=2, sticky="w", padx=5)

# Calculate final price button
btn_final = tk.Button(window, text="Final Price", command=final_price, bg="lightblue", font=("Arial",14))
btn_final.grid(row=row_index+1, column=0, columnspan=3, pady=15)

# Total price label
label_total = tk.Label(window, text=f"{currency.get()} {total_price:.2f}", bg="lightgrey", font=("Arial",14))
label_total.grid(row=row_index+2, column=0, columnspan=3, pady=(10,5))

window.mainloop()
