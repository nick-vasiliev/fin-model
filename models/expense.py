from models.period import Period


class Expense:

    def __init__(self, name: str, amount: float, period: Period):
        self.name = name
        self.amount = amount
        self.period = period
    
    def __repr__(self):
        return f"{self.name}: {self.amount} every {self.period} weeks"