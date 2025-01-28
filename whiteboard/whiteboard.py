import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from PIL import Image, ImageGrab, ImageTk


class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Whiteboard")
        self.root.geometry("800x600")

        # Initialize drawing variables
        self.line_width = 2  # Fixed initialization
        self.color = "black"
        self.drawing = False
        self.last_x = None
        self.last_y = None
        self.eraser_mode = False
        self.shape_mode = None  # New variable to track shape drawing mode
        self.start_x = None
        self.start_y = None
        self.current_shape = None

        # Create main layout
        self.create_sidebar()
        self.create_canvas()

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar = tk.Frame(self.root, width=150, bg='lightgray')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        # Color buttons
        colors = [
            "red", "orange", "yellow",
            "green", "blue", "purple",
            "black", "white"
        ]

        # Color selection frame
        color_frame = tk.Frame(self.sidebar, bg='lightgray')
        color_frame.pack(pady=10)

        # Create color buttons as square cubes
        for color in colors:
            btn = tk.Button(
                color_frame,
                bg=color,
                width=4,  # Make it wider for vertical orientation
                height=1,  # Add height for better visibility
                command=lambda c=color: self.set_color(c)
            )
            btn.pack(side=tk.TOP, padx=2, pady=2)

        # Color Picker button
        color_picker_btn = tk.Button(
            self.sidebar,
            text="Custom Color",
            command=self.open_color_picker,
            width=10
        )
        color_picker_btn.pack(pady=10)

        # Shape drawing buttons
        shape_frame = tk.Frame(self.sidebar, bg='lightgray')
        shape_frame.pack(pady=5)

        # Rectangle drawing button
        self.rect_btn = tk.Button(
            shape_frame,
            text="Rectangle",
            command=lambda: self.set_shape_mode('rectangle'),
            width=10
        )
        self.rect_btn.pack()

        # Circle drawing button
        self.circle_btn = tk.Button(
            shape_frame,
            text="Circle",
            command=lambda: self.set_shape_mode('circle'),
            width=10
        )
        self.circle_btn.pack()

        # Eraser button
        self.eraser_btn = tk.Button(
            self.sidebar,
            text="Eraser",
            command=self.toggle_eraser,
            width=10
        )
        self.eraser_btn.pack(pady=10)

        # Line width controls
        tk.Label(self.sidebar, text="Line Width", bg='lightgray').pack(pady=5)

        width_frame = tk.Frame(self.sidebar, bg='lightgray')
        width_frame.pack()

        tk.Button(width_frame, text="-", command=self.decrease_width).pack(side=tk.LEFT)
        self.width_label = tk.Label(width_frame, text=str(self.line_width), bg='lightgray')
        self.width_label.pack(side=tk.LEFT)
        tk.Button(width_frame, text="+", command=self.increase_width).pack(side=tk.LEFT)

        # Clear and Save buttons
        tk.Button(
            self.sidebar,
            text="Clear Canvas",
            command=self.clear_canvas,
            width=10
        ).pack(pady=10)

        tk.Button(
            self.sidebar,
            text="Save Image",
            command=self.save_canvas,
            width=10
        ).pack(pady=10)

    def create_canvas(self):
        # Main drawing canvas
        self.canvas = tk.Canvas(
            self.root,
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def open_color_picker(self):
        # Open color chooser dialog
        color = colorchooser.askcolor(title="Choose color")
        if color[1]:  # Check if a color was selected
            self.set_color(color[1])

    def toggle_eraser(self):
        # Toggle eraser mode with a larger default width
        self.eraser_mode = not self.eraser_mode
        self.shape_mode = None  # Reset shape mode
        if self.eraser_mode:
            # Change button appearance when eraser is active
            self.eraser_btn.config(relief=tk.SUNKEN)
            self.rect_btn.config(relief=tk.RAISED)
            self.circle_btn.config(relief=tk.RAISED)
            # Set eraser to a larger width by default
            self.line_width = 20
            self.width_label.config(text=str(self.line_width))
        else:
            # Reset button appearance
            self.eraser_btn.config(relief=tk.RAISED)
            # Reset to default line width
            self.line_width = 2
            self.width_label.config(text=str(self.line_width))

    def set_shape_mode(self, shape):
        # Reset any previous shape drawing
        if self.current_shape:
            self.canvas.delete(self.current_shape)
            self.current_shape = None

        # Toggle shape mode
        if self.shape_mode == shape:
            self.shape_mode = None
            # Reset button appearance
            self.rect_btn.config(relief=tk.RAISED)
            self.circle_btn.config(relief=tk.RAISED)
        else:
            self.shape_mode = shape
            # Highlight active shape button
            self.rect_btn.config(relief=tk.RAISED)
            self.circle_btn.config(relief=tk.RAISED)
            if shape == 'rectangle':
                self.rect_btn.config(relief=tk.SUNKEN)
            else:
                self.circle_btn.config(relief=tk.SUNKEN)

        # Ensure other modes are disabled
        self.eraser_mode = False
        self.eraser_btn.config(relief=tk.RAISED)

    def set_color(self, color):
        self.color = color
        # Disable eraser mode when selecting a color
        if self.eraser_mode:
            self.toggle_eraser()
        # Disable shape mode when selecting a color
        if self.shape_mode:
            self.set_shape_mode(self.shape_mode)

    def increase_width(self):
        if self.line_width < 50:  # Increased max width
            self.line_width += 1
            self.width_label.config(text=str(self.line_width))

    def decrease_width(self):
        if self.line_width > 1:
            self.line_width -= 1
            self.width_label.config(text=str(self.line_width))

    def start_draw(self, event):
        self.drawing = True
        self.start_x = event.x
        self.start_y = event.y
        self.last_x = event.x
        self.last_y = event.y

        # Handle shape drawing
        if self.shape_mode:
            # Start of shape drawing
            self.current_shape = None

    def draw(self, event):
        if not self.drawing:
            return

        # Freehand drawing
        if not self.shape_mode and not self.eraser_mode:
            draw_color = self.color
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                width=self.line_width,
                fill=draw_color,
                capstyle=tk.ROUND,
                smooth=tk.TRUE
            )
            self.last_x = event.x
            self.last_y = event.y

        # Shape drawing
        elif self.shape_mode:
            # Delete previous shape preview
            if self.current_shape:
                self.canvas.delete(self.current_shape)

            # Draw shape preview
            if self.shape_mode == 'rectangle':
                self.current_shape = self.canvas.create_rectangle(
                    self.start_x, self.start_y,
                    event.x, event.y,
                    outline=self.color,
                    width=self.line_width
                )
            elif self.shape_mode == 'circle':
                self.current_shape = self.canvas.create_oval(
                    self.start_x, self.start_y,
                    event.x, event.y,
                    outline=self.color,
                    width=self.line_width
                )

        # Eraser mode
        elif self.eraser_mode:
            draw_color = 'white'
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                width=self.line_width,
                fill=draw_color,
                capstyle=tk.ROUND,
                smooth=tk.TRUE
            )
            self.last_x = event.x
            self.last_y = event.y

    def stop_draw(self, event):
        # Keep shape if in shape drawing mode
        if self.shape_mode:
            # Draw the permanent shape
            if self.shape_mode == 'rectangle':
                self.canvas.create_rectangle(
                    self.start_x, self.start_y,
                    event.x, event.y,
                    outline=self.color,
                    width=self.line_width
                )
            elif self.shape_mode == 'circle':
                self.canvas.create_oval(
                    self.start_x, self.start_y,
                    event.x, event.y,
                    outline=self.color,
                    width=self.line_width
                )

            # Delete the temporary preview shape
            if self.current_shape:
                self.canvas.delete(self.current_shape)
                self.current_shape = None

        # Reset drawing variables
        self.drawing = False
        self.start_x = None
        self.start_y = None
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        # Prompt for confirmation
        if messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the entire canvas?"):
            self.canvas.delete("all")

    def save_canvas(self):
        # Open save file dialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
        )

        if file_path:
            # Create an image with the canvas contents
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            # Use PIL to save the image
            ImageGrab.grab(bbox=(x, y, x1, y1)).save(file_path)
            messagebox.showinfo("Save Successful", f"Image saved to {file_path}")


def main():
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()