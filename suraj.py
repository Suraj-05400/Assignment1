import tkinter as tk
from tkinter import ttk, messagebox


# Function to convert number
def convert_all():
    try:
        num = entry_number.get()
        base = combo_from.get()

        if base == "Binary":
            decimal = int(num, 2)
        elif base == "Octal":
            decimal = int(num, 8)
        elif base == "Hexadecimal":
            decimal = int(num, 16)
        else:
            decimal = int(num)

        # Calculate all possible conversions
        binary_result.set(bin(decimal)[2:])
        octal_result.set(oct(decimal)[2:])
        hexadecimal_result.set(hex(decimal)[2:].upper())
        decimal_result.set(str(decimal))
    except ValueError:
        messagebox.showerror("Error", "Invalid input number for the chosen base.")


# Function for addition
def add_numbers():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        addition_result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Function for subtraction
def subtract_numbers():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        subtraction_result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Function to calculate 1's complement
# Function to calculate 1's complement
def ones_complement():
    try:
        # Get the binary input
        binary_number = entry_comp.get()

        # Validate input (check if it contains only 0s and 1s)
        if not all(bit in '01' for bit in binary_number):
            raise ValueError("Please enter a valid binary number.")

        # Calculate One's Complement
        ones_comp = ''.join('1' if bit == '0' else '0' for bit in binary_number)

        # Display 1's Complement result
        complement_result.set(f"1's: {ones_comp}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Function to calculate 1's complement
def ones_complement():
    try:
        # Get the binary input
        binary_number = entry_comp.get()

        # Validate input (check if it contains only 0s and 1s)
        if not all(bit in '01' for bit in binary_number):
            raise ValueError("Please enter a valid binary number.")

        # Calculate One's Complement
        ones_comp = ''.join('1' if bit == '0' else '0' for bit in binary_number)

        # Display 1's Complement result
        ones_complement_result.set(f"1's: {ones_comp}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Function to calculate 2's complement
def twos_complement():
    try:
        # Get the binary input
        binary_number = entry_comp.get()

        # Validate input (check if it contains only 0s and 1s)
        if not all(bit in '01' for bit in binary_number):
            raise ValueError("Please enter a valid binary number.")

        # Calculate One's Complement
        ones_comp = ''.join('1' if bit == '0' else '0' for bit in binary_number)

        # Calculate Two's Complement
        twos_comp = bin(int(ones_comp, 2) + 1)[2:]

        # Display 2's Complement result
        twos_complement_result.set(f"2's: {twos_comp}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Tkinter window setup
root = tk.Tk()
root.title("Number Conversion and Operations Tool")

ones_complement_result = tk.StringVar()
twos_complement_result = tk.StringVar()

# Conversion UI
# Conversion UI
frame_conversion = ttk.LabelFrame(root, text="Conversion")
frame_conversion.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_conversion, text="Number:").grid(row=0, column=0)
entry_number = ttk.Entry(frame_conversion)
entry_number.grid(row=0, column=1)

ttk.Label(frame_conversion, text="From:").grid(row=1, column=0)
combo_from = ttk.Combobox(frame_conversion, values=["Decimal", "Binary", "Octal", "Hexadecimal"], state="readonly")
combo_from.grid(row=1, column=1)
combo_from.current(0)

ttk.Button(frame_conversion, text="Convert All", command=convert_all).grid(row=2, columnspan=2, pady=5)

# Add fields for all conversions
binary_result = tk.StringVar()
ttk.Label(frame_conversion, text="Binary:").grid(row=3, column=0)
ttk.Entry(frame_conversion, state="readonly", textvariable=binary_result).grid(row=3, column=1)

octal_result = tk.StringVar()
ttk.Label(frame_conversion, text="Octal:").grid(row=4, column=0)
ttk.Entry(frame_conversion, state="readonly", textvariable=octal_result).grid(row=4, column=1)

hexadecimal_result = tk.StringVar()
ttk.Label(frame_conversion, text="Hexadecimal:").grid(row=5, column=0)
ttk.Entry(frame_conversion, state="readonly", textvariable=hexadecimal_result).grid(row=5, column=1)

decimal_result = tk.StringVar()
ttk.Label(frame_conversion, text="Decimal:").grid(row=6, column=0)
ttk.Entry(frame_conversion, state="readonly", textvariable=decimal_result).grid(row=6, column=1)

# Arithmetic Operations UI
frame_operations = ttk.LabelFrame(root, text="Arithmetic Operations")
frame_operations.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(frame_operations, text="Number 1:").grid(row=0, column=0)
entry_num1 = ttk.Entry(frame_operations)
entry_num1.grid(row=0, column=1)

ttk.Label(frame_operations, text="Number 2:").grid(row=1, column=0)
entry_num2 = ttk.Entry(frame_operations)
entry_num2.grid(row=1, column=1)

addition_result = tk.StringVar()
ttk.Button(frame_operations, text="Add", command=add_numbers).grid(row=2, column=0)
ttk.Entry(frame_operations, state="readonly", textvariable=addition_result).grid(row=2, column=1)

subtraction_result = tk.StringVar()
ttk.Button(frame_operations, text="Subtract", command=subtract_numbers).grid(row=3, column=0)
ttk.Entry(frame_operations, state="readonly", textvariable=subtraction_result).grid(row=3, column=1)

# Complement Calculation UI
frame_complement = ttk.LabelFrame(root, text="Complement Calculation")
frame_complement.grid(row=2, column=0, padx=10, pady=10)

ttk.Label(frame_complement, text="Enter number:").grid(row=0, column=0, sticky="e")
entry_comp = ttk.Entry(frame_complement)
entry_comp.grid(row=0, column=1, sticky="w")

# 1's Complement Button and Result
ttk.Button(frame_complement, text="1's Complement", command=ones_complement).grid(row=1, column=0, sticky="ew")
ttk.Entry(frame_complement, state="readonly", textvariable=ones_complement_result).grid(row=1, column=1, sticky="ew")

# 2's Complement Button and Result
ttk.Button(frame_complement, text="2's Complement", command=twos_complement).grid(row=2, column=0, sticky="ew")
ttk.Entry(frame_complement, state="readonly", textvariable=twos_complement_result).grid(row=2, column=1, sticky="ew")

root.mainloop()