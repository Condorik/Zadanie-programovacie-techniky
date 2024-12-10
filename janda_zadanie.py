import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, Frame, PhotoImage

# Globálna premenná na nastavenie počtu generovaných čísel
num_values = 20

def generate_and_plot():
    global num_values
    try:
        # Generovanie poľa num_values náhodných desatinných čísel v intervale [-10, 10]
        random_numbers = np.random.uniform(-10, 10, num_values)

        # Zaokrúhlenie každého čísla na celé číslo
        rounded_numbers = np.round(random_numbers)

        # Počítanie kladných a záporných čísel
        positive_count = np.sum(rounded_numbers > 0)
        negative_count = np.sum(rounded_numbers < 0)

        # Zobrazenie počtu kladných a záporných čísel v konzole
        print(f"Počet kladných čísiel: {positive_count}")
        print(f"Počet záporných čísiel: {negative_count}")

        # Vykreslenie grafu hodnôt
        plt.figure(figsize=(10, 6))
        plt.bar(range(1, num_values + 1), rounded_numbers, color=['green' if x > 0 else 'red' for x in rounded_numbers])
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.title("Graf hodnôt zaokrúhlených čísel")
        plt.xlabel("Index čísla")
        plt.ylabel("Hodnota čísla")
        plt.xticks(range(1, num_values + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    except Exception as e:
        print(f"Chyba: {e}")

def update_param():
    global num_values
    try:
        # Aktualizácia parametra na základe vstupu používateľa
        new_value = int(param_entry.get())
        if new_value > 0:
            num_values = new_value
            print(f"Počet generovaných čísiel bol nastavený na: {num_values}")
        else:
            print("Zadajte kladné číslo!")
    except ValueError:
        print("Zadajte platné celé číslo!")

# Vytvorenie hlavného okna GUI
root = Tk()
root.title("Zadanie úlohy - Programovacie techniky")
root.geometry("1300x400")

# Rámec pre textové prvky a tlačidlá
frame = Frame(root)
frame.pack(side="left", padx=10, pady=10)

# Pridanie názvu a informácií do GUI
Label(frame, text="Programovacie techniky", font=("Arial", 16, "bold")).pack(pady=5)
Label(frame, text="Šimon Janda", font=("Arial", 12)).pack(pady=5)
Label(frame, text="Zadanie úlohy:", font=("Arial", 12, "bold")).pack(pady=5)
Label(frame, text=(
    "Vygenerujte pole náhodných desatinných čísiel z intervalu -10 až 10,\n"
    "každé z nich zaokrúhlite na celé číslo, vypíšte počet záporných a kladných čísiel,\n"
    "a zobrazte graf hodnôt."
), font=("Arial", 10), justify="left").pack(pady=10)

# Pridanie vstupu na zmenu parametrov
Label(frame, text="Zadajte počet generovaných čísiel:", font=("Arial", 10)).pack(pady=5)
param_entry = Entry(frame, width=10)
param_entry.pack(pady=5)

# Tlačidlá
update_button = Button(frame, text="Zmeniť parameter", command=update_param, padx=10, pady=5)
update_button.pack(pady=5)

run_button = Button(frame, text="Spustiť program", command=generate_and_plot, padx=20, pady=10)
run_button.pack(pady=20)

# Pridanie obrázka do pravého horného rohu
try:
    img = PhotoImage(file="foto.png")  # Obrázok s názvom con.png
    image_label = Label(root, image=img)
    image_label.pack(side="right", padx=10, pady=10)
except Exception as e:
    print(f"Chyba pri načítaní obrázka: {e}")

# Spustenie hlavnej slučky GUI
root.mainloop()
