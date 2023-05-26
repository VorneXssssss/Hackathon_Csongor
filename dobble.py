import sys
import random

def generate_dobble(n):
    if n < 1:
        print("Hibás bemeneti paraméter!")
        return

    prev_row = []
    current_row = []
    esely = 90  #több esély az azonos számokra

    while True:
        current_row = []
        while len(current_row) < n:
            number = random.randint(1, 50)
            if number not in current_row:
                current_row.append(number)

        if len(prev_row) > 0 and len(set(prev_row) & set(current_row)) == 0:
            if random.randint(1, 100) <= esely:
                random_index = random.randint(0, n - 1)
                current_row[random_index] = prev_row[random_index]
            else:
                break

        prev_row = current_row.copy()
        print(" ".join(str(num) for num in current_row))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Használat: python dobble.py <n>")
    else:
        try:
            n = int(sys.argv[1])
            generate_dobble(n)
        except ValueError:
            print("Hibás bemeneti paraméter!")
