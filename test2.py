import tkinter as tk
from tkinter import messagebox
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_equation():
    eq = entry.get().strip()
    if not eq:
        messagebox.showwarning("Error", "Please enter an equation.")
        return
        
    try:
        x = np.linspace(-10, 10, 100)
        context = {
            "x": x, "sin": np.sin, "cos": np.cos, 
            "tan": np.tan, "sqrt": np.sqrt, "pi": np.pi
        }
        y = eval(eq, {"__builtins__": None}, context)
        
        ax.clear()
        ax.plot(x, y, color="black", linewidth=2)
        ax.grid(True)
        ax.set_title(f"y = {eq}")
        canvas.draw()
    except Exception:
        messagebox.showerror("Math Error", "Invalid syntax. Use 'x' (e.g., x**2, sin(x)).")

root = tk.Tk()
root.title("Graphing App")
root.geometry("600x500")

# Direct relative path since it's inside your project directory
try:
    root.iconbitmap("image.ico")
except Exception:
    pass

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=50, y=10, width=500, height=350)

tk.Label(root, text="Equation:", font=("Arial", 11)).place(x=50, y=390)

entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.insert(0, "x**2") 
entry.place(x=50, y=415, height=30)

plot_btn = tk.Button(root, text="Plot", command=plot_equation, bg="black", fg="white", font=("Arial", 10, "bold"))
plot_btn.place(x=260, y=415, width=100, height=30)

if __name__ == "__main__":
    root.mainloop()
