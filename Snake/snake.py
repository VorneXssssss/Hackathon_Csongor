import random

# Játékmező méretei
width = 60
height = 30

# Jelölések a játékhoz
snake_head = "@"    # Kígyó feje
fence = "*"         # Kerítés
empty_space = " "   # Üres hely

# Játékmező
board = [[fence if x == 0 or x == width-1 or y == 0 or y == height-1 else empty_space for x in range(width)] for y in range(height)]

# Kígyó kezdeti pozíciója
snake_x = random.randint(1, width-2)
snake_y = random.randint(1, height-2)
board[snake_y][snake_x] = snake_head

# Játékmező megjelenítése
def display_board():
    for row in board:
        print("".join(row))

# Kígyó mozgatása
def move_snake(x, y):
    if board[y][x] == fence:
        print("Sajnos, a piton nekiment a kerítésnek! Most ennyi volt, szép napot!")
        return True
    board[snake_y][snake_x] = empty_space
    board[y][x] = snake_head
    return False

# Játék indítása
print("Snake játék!")
display_board()
print("Hova?")

game_over = False
while not game_over:
    direction = input("> ")

    # Kígyó mozgatása a megadott irányba
    if direction == "balra":
        game_over = move_snake(snake_x - 1, snake_y)
        snake_x -= 1
    elif direction == "jobbra":
        game_over = move_snake(snake_x + 1, snake_y)
        snake_x += 1
    elif direction == "fel":
        game_over = move_snake(snake_x, snake_y - 1)
        snake_y -= 1
    elif direction == "le":
        game_over = move_snake(snake_x, snake_y + 1)
        snake_y += 1
    elif direction == "meguntam":
        game_over = True
        print("Most ennyi volt, szép napot!")

    # Játékmező megjelenítése és következő lépés bekérése
    if not game_over:
        display_board()
        print("Hova? (balra, jobbra, fel, le, vagy meguntam)")
