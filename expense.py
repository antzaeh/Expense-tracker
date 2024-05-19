class Expense:
    def __init__(self, category,description, price, date):
        self.category = category
        self.description = description
        self.price = price
        self.date = date

    def __str__(self):
        return f"Category: {self.category}, Description: {self.description}, Price: {self.price}, Date: {self.date}"