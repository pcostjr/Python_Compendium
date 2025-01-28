import tkinter as tk
import random


class CanvasDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Exploration")
        self.root.geometry("500x400")

        # Create canvas
        self.canvas = tk.Canvas(
            root,
            bg='white',
            width=400,
            height=300
        )
        self.canvas.pack(pady=20)

        # Buttons for drawing
        frame = tk.Frame(root)
        frame.pack()

        # Draw Rectangle Button
        tk.Button(
            frame,
            text="Draw Rectangle",
            command=self.draw_rectangle
        ).pack(side=tk.LEFT, padx=5)

        # Draw Circle Button
        tk.Button(
            frame,
            text="Draw Circle",
            command=self.draw_circle
        ).pack(side=tk.LEFT, padx=5)

        # Clear Canvas Button
        tk.Button(
            frame,
            text="Clear Canvas",
            command=self.clear_canvas
        ).pack(side=tk.LEFT, padx=5)

    def draw_rectangle(self):
        x1 = random.randint(50, 250)
        y1 = random.randint(50, 200)
        x2 = x1 + random.randint(50, 100)
        y2 = y1 + random.randint(50, 100)
        color = f'#{random.randint(0, 0xFFFFFF):06x}'

        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline='black'
        )

    def draw_circle(self):
        x1 = random.randint(50, 250)
        y1 = random.randint(50, 200)
        radius = random.randint(20, 50)
        color = f'#{random.randint(0, 0xFFFFFF):06x}'

        self.canvas.create_oval(
            x1 - radius, y1 - radius,
            x1 + radius, y1 + radius,
            fill=color,
            outline='black'
        )

    def clear_canvas(self):
        self.canvas.delete('all')


def main():
    root = tk.Tk()
    app = CanvasDemoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()