import tkinter as tk

class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Demo")
        self.root.geometry("300x250")

        # Counter to track button clicks
        self.click_count = 0

        # Create a label to show clicks
        self.label = tk.Label(
            root,
            text="Clicks: 0",
            font=("Arial", 14)
        )
        self.label.pack(pady=20)

        # Create buttons
        self.click_button = tk.Button(
            root,
            text="Click Me!",
            command=self.increment_click
        )
        self.click_button.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(
            root,
            text="Reset",
            command=self.reset_click
        )
        self.reset_button.pack(pady=10)

    def increment_click(self):
        self.click_count += 1
        self.label.config(text=f"Clicks: {self.click_count}")

    def reset_click(self):
        self.click_count = 0
        self.label.config(text="Clicks: 0")

def main():
    root = tk.Tk()
    app = ButtonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()