import math


class CalculatorModel:
    def __init__(self):
        self.valeur =""

    
    def add(self, op):
        self.valeur += op
        return self.valeur
    
    def racine(self, op):
        try:
            nombre = eval(self.valeur)
            self.valeur = str(math.sqrt(nombre))
            return self.valeur
        except Exception:
            return "Erreur"



    
    def calculate(self):
        try:
            result = str(eval(self.valeur))
            return result
        except Exception:
            return "Erreur"
        

    
    