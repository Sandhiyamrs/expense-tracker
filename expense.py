class Expense:
    def __init__(self, amount, category, date, note):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note
        }