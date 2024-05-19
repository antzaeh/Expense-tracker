import datetime
import pickle
from typing import List
from expense import Expense


class ExpenseTracker:
    expenseList: List[Expense] = []
    fileName = "expense.dat"

    @staticmethod
    def main_menu():
        intro = ('Number:\n'
                 "1. New expense\n"
                 "2. Show today's expense\n"
                 "3. Search by date\n"           
                 "4. Save/Load to/from file\n"
                 "X. Exit")
        ExpenseTracker.read_from_file()
        print(intro)
        
        while True:
            user_input = input().lower()
            if user_input == '1':
                ExpenseTracker.new_expense()
            elif user_input == '2':
                ExpenseTracker.todays_expense()
            elif user_input == '3':
                ExpenseTracker.expense_by_date()
            elif user_input == '4':
                ExpenseTracker.file_mode()
            elif user_input == 'x':
                ExpenseTracker.save_to_file()
                break
            else:
                print("Incorrect input")
            print(intro)

    @staticmethod
    def new_expense():
        chooseCategory = ("Choose category:\n"
                          "1. Car\n"
                          "2. Bill\n"
                          "3. Shop\n"
                          "4. Entertainment\n"
                          "5. Misc\n"
                          "0. Return")
        
        date = input("Enter date dd.mm.yyyy: ")

        while True:
            print(chooseCategory)
            category_input = input().lower()
            if category_input == '1':
                category = "Car"
            elif category_input == '2':
                category = "Bill"
            elif category_input == '3':
                category = "Shop"
            elif category_input == '4':
                category = "Entertainment"
            elif category_input == '5':
                category = "Misc"
            elif category_input == '0':
                return
            else:
                print("Incorrect input")
                continue

            try:
                price = float(input("Enter price, separate decimals with dot: "))
                description = input("Description: ")
                ExpenseTracker.add_new_expense(date, price, description, category)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
                continue
            break

    @staticmethod
    def add_new_expense(date, price, description, category):
        ExpenseTracker.expenseList.append(Expense(category, description, price, date))

    @staticmethod
    def todays_expense():
        today = datetime.date.today()
        formatted_date = today.strftime("%d.%m.%Y")
        today_sum = 0
        for expense in ExpenseTracker.expenseList:
            if expense.date == formatted_date:
                today_sum += expense.price
                print(expense)              
        print(f"Todays expense: {today_sum}")

    @staticmethod
    def expense_by_date():
        date_to_find = input("Enter date dd.mm.yyyy: ")
        found = False
        for expense in ExpenseTracker.expenseList:
            if expense.date == date_to_find:
                print(expense)
                found = True
        if not found:
            print(f"Nothing for {date_to_find}")

    @staticmethod
    def file_mode():
        print("1 to load from file\n2 to save into file")
        file_mode_input = input().lower()
        if file_mode_input == '1':
            ExpenseTracker.read_from_file()
        elif file_mode_input == '2':
            ExpenseTracker.save_to_file()
        else:
            print("Incorrect input")

    @staticmethod
    def read_from_file():
        fileName = ExpenseTracker.fileName
        try:
            with open(fileName, "rb") as file:
                ExpenseTracker.expenseList = pickle.load(file)
            print(f"{fileName} loaded successfully")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Problem with loading from {fileName}")
            print(e)

    @staticmethod
    def save_to_file():
        fileName = ExpenseTracker.fileName
        try:
            with open(fileName, "wb") as file:
                pickle.dump(ExpenseTracker.expenseList, file)
            print(f"Save successful to {fileName}")
        except Exception as e:
            print(f"Problem with saving to {fileName}")
            print(e)

if __name__ == "__main__":
    ExpenseTracker.main_menu()
