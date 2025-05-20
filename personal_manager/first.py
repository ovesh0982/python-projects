import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store data
data_file = "finance_data.csv"

# Function to initialize the CSV file if it doesn't exist
def initialize_data_file():
    if not os.path.exists(data_file):
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Description"])

# Function to add a new transaction (income or expense)
def add_transaction():
    type_ = transaction_type.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if amount == "" or not amount.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return

    amount = float(amount)

    # Write the transaction to the CSV file
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([type_, amount, description])

    update_summary()

    # Clear the input fields
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Function to update the summary of total income, expenses, and balance
def update_summary():
    total_income = 0
    total_expenses = 0

    # Read all transactions from the CSV file
    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            type_, amount, _ = row
            amount = float(amount)
            if type_ == "Income":
                total_income += amount
            elif type_ == "Expense":
                total_expenses += amount

    balance = total_income - total_expenses

    # Update the labels in the GUI
    income_label.config(text=f"Total Income: ${total_income:.2f}")
    expenses_label.config(text=f"Total Expenses: ${total_expenses:.2f}")
    balance_label.config(text=f"Remaining Balance: ${balance:.2f}")

# Function to show the transaction history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Transaction History")

    # Create a listbox to display the history
    history_listbox = tk.Listbox(history_window, width=50, height=10)
    history_listbox.pack(pady=20)

    # Read and display all transactions from the CSV file
    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            type_, amount, description = row
            history_listbox.insert(tk.END, f"{type_}: ${amount} - {description}")

# Setting up the GUI window
root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x400")

# Labels to show total income, expenses, and balance
income_label = tk.Label(root, text="Total Income: $0.00", font=("Arial", 12))
income_label.pack(pady=10)

expenses_label = tk.Label(root, text="Total Expenses: $0.00", font=("Arial", 12))
expenses_label.pack(pady=10)

balance_label = tk.Label(root, text="Remaining Balance: $0.00", font=("Arial", 12))
balance_label.pack(pady=10)

# Entry for the amount and description
amount_label = tk.Label(root, text="Amount ($):", font=("Arial", 12))
amount_label.pack(pady=5)

amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=5)

description_label = tk.Label(root, text="Description:", font=("Arial", 12))
description_label.pack(pady=5)

description_entry = tk.Entry(root, font=("Arial", 12))
description_entry.pack(pady=5)

# Dropdown to select income or expense
transaction_type = tk.StringVar(root)
transaction_type.set("Income")
type_dropdown = tk.OptionMenu(root, transaction_type, "Income", "Expense")
type_dropdown.pack(pady=5)

# Button to add a transaction
add_button = tk.Button(root, text="Add Transaction", font=("Arial", 12), command=add_transaction)
add_button.pack(pady=10)

# Button to view transaction history
history_button = tk.Button(root, text="Show Transaction History", font=("Arial", 12), command=show_history)
history_button.pack(pady=10)

# Initialize the CSV file and update the summary
initialize_data_file()
update_summary()

# Run the Tkinter event loop
root.mainloop()
