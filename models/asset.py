class Asset:

    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"{self.name}: {self.value}"
