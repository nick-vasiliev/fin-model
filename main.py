"""
main app
"""
from models import Income, Period, Expense, Asset
from scenarios import Scenario
from scenarios.economic import inflation

from engine import FinancialModel

def job_loss(model: FinancialModel):
    """
    Simulate job loss by removing the main income source.
    """
    max_income = Income("Default", 0, Period.WEEKLY)
    for income in model.incomes:
        if income > max_income:
            max_income = income
    model.incomes.remove(max_income)
    return {
        "job": max_income
    }

def time_unemployed(model: FinancialModel, iteration: int, **kwargs):
    """
    Simulate being unemployed for a certain number of months.

    iteration: int - current iteration (week) of the Scenario applying this function

    kwargs:
        iterations_unemployed: int - number of iterations (weeks) to be unemployed for
        job: Income - the job to be added back after the unemployment period is over
    """
    # First remove the job
    if iteration == 0:
        return kwargs | job_loss(model)
    
    # Add the job back after the iterations_unemployed is reached
    elif iteration == kwargs.get("iterations_unemployed"):
        model.add_income(kwargs.get("job"))
        return kwargs | {"job": None}
    return kwargs

if __name__ == "__main__":
    print("===========")

    six_months_unemployed_scenario = Scenario(
        time_unemployed,
        iterations_unemployed=26,
    )
    model = FinancialModel(starting_cash=0)
    model.add_income(Income("Job", 1000, Period.WEEKLY))
    model.add_scenario(six_months_unemployed_scenario)
    model.add_scenario(Scenario(inflation.high_inflation))
    for _ in range(52):
        model.run()
    
