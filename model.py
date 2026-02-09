import math


class CalculatorModel:
    def __init__(self):
        self.valeur =""

    
    def add(self, op):
        self.valeur += op
        return self.valeur
    
    def racine(self):
        self.valeur = math.sqrt(self.valeur)
        return self.valeur

    
    def calculate(self):
        try:
            result = str(eval(self.valeur))
            return result
        except Exception:
            return "Erreur"
        

    
    