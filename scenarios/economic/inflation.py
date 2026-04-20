"""
Simulates various levels of inflation.
"""

from engine import FinancialModel
from random import random
from models import Period

def high_inflation(model: FinancialModel, iteration: int, **kwargs):
    """
    Simulates a scenario with high inflation (relative to RBA target of 3%).
    
    Aims to weigh higher levels of inflation as more likely, but with a long tail of lower levels of inflation.
    """
    if iteration % Period.YEARLY.value != 0: # only update inflation rate yearly
        return kwargs
    
    change_range = 0.025 # range of possible changes in inflation rate (e.g. 0.025 means the inflation rate can change by up to 2.5% in either direction)
    inflation_rate = kwargs.get("inflation_rate", 0.03)  # default to 3% inflation rate (on first iteration)
    
    inflation_rate += 4*change_range*random()**2 - change_range # parabolic so weighs more on higher inflation
    print(f"Inflation rate: {inflation_rate:.2%}")
    return {"inflation_rate": inflation_rate}