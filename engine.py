from models import Income, Expense, Asset
from scenarios import Scenario

class FinancialModel:
    
    def __init__(self, starting_cash: float = 0):
        self.cash = Asset("Cash", starting_cash)
        self.assets = []
        self.incomes = []
        self.expenses = []
        self.scenarios = []
        self.iterations = 0

    # Incomes
    def add_income(self, income: Income):
        self.incomes.append(income)
    
    def _apply_income(self):
        """
        Apply incomes to cash (ignoring tax) for this iteration
        """
        for income in self.incomes:
            if self.iterations % income.period.value == 0:
                self.cash.value += income.amount
    
    # Expenses
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def _apply_expenses(self):
        """
        Apply expenses to cash for this iteration
        """
        for expense in self.expenses:
            if self.iterations % expense.period.value == 0:
                self.cash.value -= expense.amount
    
    # Assets
    # TODO: changes in value and dividends, 
    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    # Scenarios
    def add_scenario(self, scenario: Scenario):
        self.scenarios.append(scenario)
    
    def _apply_scenarios(self):
        for scenario in self.scenarios:
            scenario.run(self)
    
    def run(self):
        """
        Simulate 1 week (iteration)
        """
        self.iterations += 1
        self._apply_scenarios()

        self._apply_expenses()
        self._apply_income()