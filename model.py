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
    def divide(self, a,b):
        if b==0:
            return "cannot divide by zero"
        else:
            return a/b

    def calculate(self):
        try:
            result = str(eval(self.valeur.replace('÷', '/').replace('×', '*').replace('^', '**')))
            return result
        except Exception:
            return "Erreur"
        

    
    