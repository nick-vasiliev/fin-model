
from models.period import Period

class Income:

    def __init__(self, name: str, amount: float, period: Period, tax_free_threshold: bool = False):
        self.name = name
        self.amount = amount
        self.period = period
        self.tax_free_threshold = tax_free_threshold
    
    def get_yearly_amount(self) -> float:
        """Convert the income amount to a yearly amount based on the period."""
        return self.amount * (52 / self.period.value)
    
    def __repr__(self):
        return f"{self.name}: {self.amount} every {self.period} weeks"
    
    # COMPARISON FUNCTIONS USING YEARLY INCOME
    def __eq__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() == other.get_yearly_amount()
    
    def __lt__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() < other.get_yearly_amount()
    
    def __le__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() <= other.get_yearly_amount()
    
    def __gt__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() > other.get_yearly_amount()
    
    def __ge__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() >= other.get_yearly_amount()
    
    def __ne__(self, other):
        if not isinstance(other, Income):
            return NotImplemented
        return self.get_yearly_amount() != other.get_yearly_amount()
    
    """
    TODO: Tax
    https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-1-statement-of-formulas-for-calculating-amounts-to-be-withheld/coefficients-to-use-in-formulas-for-withholding-from-weekly-payments
    https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-1-statement-of-formulas-for-calculating-amounts-to-be-withheld/working-out-the-weekly-earnings#offset   
    """