import sys
import random

# Dobble kártya generálása
def generate_dobble(n):
    if n < 1:
        print("Hibás bemeneti paraméter!")  # Hibaüzenet, ha a paraméter helytelen
        return

    prev_row = []  # Előző sor
    current_row = []  # Jelenlegi sor
    esely = 90  # Több esély az azonos számokra

    while True:
        current_row = []
        while len(current_row) < n:
            number = random.randint(1, 50)  # Véletlenszerű szám generálása 1 és 50 között
            if number not in current_row:
                current_row.append(number)

        # Azonos számok kicserélése vagy vége a generálásnak
        if len(prev_row) > 0 and len(set(prev_row) & set(current_row)) == 0:
            if random.randint(1, 100) <= esely:
                random_index = random.randint(0, n - 1)  # Véletlenszerű index választása
                current_row[random_index] = prev_row[random_index]  # Az azonos indexű számok kicserélése
            else:
                break

        prev_row = current_row.copy()
        print(" ".join(str(num) for num in current_row))  # Jelenlegi sor kiírása

# Program futtatása a parancssorból kapott bemenettel
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Használat: python dobble.py <n>")  # Hibaüzenet, ha a paraméterek helytelenek
    else:
        try:
            n = int(sys.argv[1])  # A parancssorból kapott bemeneti paraméter konvertálása egész számmá
            generate_dobble(n)  # Dobble kártya generálása a bemeneti paraméter alapján
        except ValueError:
            print("Hibás bemeneti paraméter!")  # Hibaüzenet, ha a bemeneti paraméter érvénytelen
