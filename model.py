import math


class CalculatorModel:
    def __init__(self):
        self.valeur =""

    
    def add(self, op):
        self.valeur += op
        return self.valeur
    
    def racine(self):
     try:
        nombre_pur = self.valeur[1:] 
        
        val = float(nombre_pur)
        if val < 0:
            return "Erreur"
            
        result = str(math.sqrt(val))
        self.valeur = result
        return result
     except Exception:
        return "Erreur"
     
    def calculate(self):
        try:
            result = str(eval(self.valeur))
            return result
        except Exception:
            return "Erreur"
        

    
    