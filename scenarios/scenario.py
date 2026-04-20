from typing import Callable

from typing import TYPE_CHECKING
if TYPE_CHECKING: # https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
    from engine import FinancialModel
    # TODO: can I avoid a circular import?  

class Scenario:
    """
    A scenario that affects the financial model.
    Multiple scenarios can affect the model at the same time, so they do not "lock" the model.

    The kwargs can be used to pass additional parameters to func.
    """
    def __init__(self, func: Callable, **kwargs):
        self.func = func
        self.kwargs = kwargs
        self.iteration = 0  # How many iterations has this scenario been active?

    def run(self, model: "FinancialModel"):
        result = self.func(model, self.iteration, **self.kwargs)
        self.kwargs = self.kwargs | result  # combine the result into the existing kwargs
        self.iteration += 1
    
    # TODO: some sort of handling to destroy the scenario when it goes inactive.