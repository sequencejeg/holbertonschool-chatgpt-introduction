#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        if mines >= self.total_cells:
            raise ValueError("Number of mines must be less than the total number of cells.")
        self.mines = set()
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_cells = 0
        self.place_mines()

    def place_mines(self):
        while len(self.mines) < 10:
            mine_pos = random.randint(0, self.total_cells - 1)
            if mine_pos not in self.mines:
                self.mines.add(mine_pos)

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height) or self.revealed[y][x]:
            return True  # Out of bounds or already revealed, do nothing

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True
        self.revealed_cells += 1

        if self.count_mines_nearby(x, y) == 0:
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = cx + dx, cy + dy
                        if (0 <= nx < self.width and 0 <= ny < self.height and
                                not self.revealed[ny][nx]):
                            if self.count_mines_nearby(nx, ny) == 0:
                                stack.append((nx, ny))
                            self.revealed[ny][nx] = True
                            self.revealed_cells += 1

        return True

    def check_victory(self):
        return self.revealed_cells == self.total_cells - len(self.mines)

    def play(self):
        first_move = True
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Invalid coordinates. Please enter numbers within the grid.")
                    continue

                if first_move:
                    # Ensure the first move is not on a mine
                    while (y * self.width + x) in self.mines:
                        print("The chosen cell is a mine. Choose a different cell.")
                        x = int(input("Enter x coordinate: "))
                        y = int(input("Enter y coordinate: "))

                    first_move = False

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_victory():
                    self.print_board(reveal=True)
                    print("Congratulations! You've cleared all the mines!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
