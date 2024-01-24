import tkinter as tk


class Hada():
    def __init__(self, position, color):
        self.head = position
        self.color = color
        self.body = [[position[0] + 1, position[1]]]
        self.direction = [0, -1]
        canvas.create_rectangle(self.head[0], self.head[1], self.head[0] + 1, self.head[1] + 1, fill=self.color)
        window.after(350, self.move)

    def move(self):
        self.head[0] += self.direction[0]*2
        self.head[1] += self.direction[1]*2
        if self.head in self.body:
            game_over()
        elif not (0 <= self.head[0] <= 300 and 0 <= self.head[1] <= 300):
            game_over()
        else:
            temp = [self.head[0], self.head[1]]
            self.body.append(temp)
            canvas.create_rectangle(self.head[0], self.head[1], self.head[0] + 1, self.head[1] + 1, fill=self.color)
            window.after(150, self.move)

    def change_direction(self, input):
        input = input.char
        if input == "w" and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif input == "s" and self.direction != [0, -1]:
            self.direction = [0, 1]
        elif input == "a" and self.direction != [1, 0]:
            self.direction = [-1, 0]
        elif input == "d" and self.direction != [-1, 0]:
            self.direction = [1, 0]


def game_over():
    canvas.create_text(150, 150, text="Game Over", font=("Arial", 30), fill="red", anchor="center")

window = tk.Tk()
window.title("1, 3, 6")
window.geometry("300x300")

canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

hada = Hada([150, 150], "black")

canvas.bind("<Key>", hada.change_direction)
canvas.focus_set()

tk.mainloop()
