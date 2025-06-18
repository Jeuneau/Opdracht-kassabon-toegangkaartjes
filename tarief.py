class Tarief :
    def __init__(self, id, naam, prijs):
        self.id = id
        self.naam = naam
        self.prijs = prijs

    def __str__(self):
        return f"Tarief(id={self.id}, naam='{self.naam}', prijs={self.prijs})"

    def __repr__(self):
        return self.__str__()
    
    