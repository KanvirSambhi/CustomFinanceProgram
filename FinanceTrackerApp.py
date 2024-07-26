import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# finance tracker script
class FinanceTracker:

    # initializing self with specific variables
    def __init__(self):
        self.budget = 0
        self.income = 0
        self.expenses = []
        self.savings_goal = 0

    # sets budget
    def set_budget(self, budget):
        self.budget = budget

    # sets income
    def set_income(self, income):
        self.income = income

    # adds expenses
    def add_expense(self, expense):
        self.expenses.append(expense)

    # adds savings goal
    def set_savings_goal(self, savings_goal):
        self.savings_goal = savings_goal

    # calculates total expenses
    def calculate_total_expenses(self):
        return sum(self.expenses)

    # summarizes all data into one block of code
    def summary(self):
        total_expenses = self.calculate_total_expenses()
        remaining_budget = self.budget - total_expenses
        data = {
            'Budget': [self.budget],
            'Income': [self.income],
            'Total Expenses': [total_expenses],
            'Remaining Budget': [remaining_budget],
            'Savings Goal': [self.savings_goal]
        }
        return pd.DataFrame(data)

    # saves all data into a .csv file so can be accessed later
    def save_summary(self, filename):
        summary_df = self.summary()
        try:
            summary_df.to_csv(filename, index=False)
            print(f"Summary saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

# code for the finance tracker app to run the application
class FinanceTrackerApp:
    def __init__(self, root):
        # initializing finance tracker app
        self.tracker = FinanceTracker()
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry('500x500')  # Set the window size to 500x500
        self.root.resizable(0, 1)

        # text to show Budget category
        self.budget_label = tk.Label(root, text="Budget:")
        self.budget_label.pack()
        # button for budget to select it
        self.budget_button = tk.Button(root, text="Set Budget", command=self.set_budget)
        self.budget_button.pack()

        # text to show income category
        self.income_label = tk.Label(root, text="Income:")
        self.income_label.pack()
        # button for income to select it
        self.income_button = tk.Button(root, text="Set Income", command=self.set_income)
        self.income_button.pack()

        # button for expenses to select it
        self.expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.expense_button.pack()

        # text to show savings goal category
        self.savings_goal_label = tk.Label(root, text="Savings Goal:")
        self.savings_goal_label.pack()
        # button to show savings goal button
        self.savings_goal_button = tk.Button(root, text="Set Savings Goal", command=self.set_savings_goal)
        self.savings_goal_button.pack()

        # button to show summary of all categories
        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.pack()

        # button to save all categories to csv file
        self.save_button = tk.Button(root, text="Save Summary to File", command=self.save_summary)
        self.save_button.pack()

    # sets the budget and asks to input budget
    def set_budget(self):
        budget = simpledialog.askfloat("Input", "Enter your budget:")
        if budget is not None:
            self.tracker.set_budget(budget)
            messagebox.showinfo("Info", f"Budget set to {budget}")

    # sets the income and asks to input income
    def set_income(self):
        income = simpledialog.askfloat("Input", "Enter your income:")
        if income is not None:
            self.tracker.set_income(income)
            messagebox.showinfo("Info", f"Income set to {income}")

    # asks to add an expense and totals them together
    def add_expense(self):
        expense = simpledialog.askfloat("Input", "Enter an expense:")
        if expense is not None:
            self.tracker.add_expense(expense)
            messagebox.showinfo("Info", f"Expense of {expense} added")

    # sets savings goal and asks for input of savings goal
    def set_savings_goal(self):
        savings_goal = simpledialog.askfloat("Input", "Enter your savings goal:")
        if savings_goal is not None:
            self.tracker.set_savings_goal(savings_goal)
            messagebox.showinfo("Info", f"Savings goal set to {savings_goal}")

    # shows the summary on screen
    def show_summary(self):
        summary = self.tracker.summary().to_string(index=False)
        messagebox.showinfo("Summary", summary)

    # saves the summary onto a file
    def save_summary(self):
        filename = simpledialog.askstring("Input", "Enter the filename to save the summary:")
        if filename:
            self.tracker.save_summary(filename)
            messagebox.showinfo("Info", f"Summary saved to {filename}")

# runs the program
if __name__ == "__main__":
    # code to initialize the application
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()