# fin-model
I made this to model out some scenarios from my personal finances. I enjoyed building it so plan to flesh it out and make it more robust.

# Code Structure
## engine.py
Contains the *FinancialModel* class that allows the simulation of cash flows and scenarios.


A FinancialModel represents a persons financial situation, encompassing cash flows, assets held and scenarios they are undergoing.


Every FinancialModel has an *Asset* dedicated to cash which changes depending on *incomes* and *expenses* over *iterations*.
Other *Asset*s can also be part of the model. *Scenario*s can also be applied to the model

## Models
Data Classes
### Asset
Thing(s) with a value, e.g. Cash, Property, a stock portfolio.

### Expense
Something that subtracts from the *cash* of a financial model periodically.

### Income
Something that adds to the *cash* of a financial model periodically.

### Period
An enum for different periods used in the models.

## Scenarios
### Scenario
A class that holds a function that is applied to a *FinancialModel* every iteration. It also has kwargs that store metadata that are passed to the scenario to control the scenario.


I'm not sure if the Scenario is built in the best way. For what I can think of now this is the best way to have modular "things" that can affect the model for certain periods.
It can definitely be optimised by tracking something like when the scenario goes inactive.
There is a concern that two functions in a scenario use the same named keyword argument, so that's also not great.