# A simple calculator GUI using Tkinter

# Import the tkinter library for GUI components
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Calculator")

# Create the entry widget for displaying input and results
entry = tk.Entry(
    root,                # Parent window
    width=16,            # Number of characters wide
    font=('timesnewroman', 25),  # Font and size
    borderwidth=2,       # Border thickness
    relief='ridge',      # Border style
    justify='right'      # Text alignment
)
# Place the entry widget at the top, spanning 4 columns
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Set the size of the window
root.geometry("450x500")

# Set the background color of the window
root.configure(bg="lightblue")  # Change to your preferred color

# Define what happens when a number or operator button is clicked
def on_click(char):
    entry.insert(tk.END, char)  # Add the character to the entry box

# Define what happens when the clear button is clicked
def clear():
    entry.delete(0, tk.END)     # Remove all text from the entry box

# Define what happens when the equals button is clicked
def calculate():
    try:
        # Evaluate the expression in the entry box
        result = eval(entry.get())
        entry.delete(0, tk.END)         # Clear the entry box
        entry.insert(tk.END, str(result)) # Show the result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")   # Show "Error" if calculation fails

# List of all calculator buttons and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)  # '=' button spans 4 columns
]

# Create and place each button on the window
for (text, row, col, *span) in buttons:
    if text == '=':
        # The equals button is extra wide and calls calculate()
        btn = tk.Button(root, text=text, width=34, height=2, font=('Arial', 14), command=calculate)
        btn.grid(row=row, column=col, columnspan=span[0], padx=2, pady=2)
    elif text == 'C':
        # The clear button calls clear()
        btn = tk.Button(root, text=text, width=8, height=2, font=('Arial', 14), command=clear)
        btn.grid(row=row, column=col, padx=2, pady=2)
    else:
        # All other buttons add their character to the entry box
        btn = tk.Button(root, text=text, width=8, height=2, font=('Arial', 14), command=lambda t=text: on_click(t))
        btn.grid(row=row, column=col, padx=2, pady=2)

# Start the Tkinter event loop (keeps the window open)
root.mainloop()