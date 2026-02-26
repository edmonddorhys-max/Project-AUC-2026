import math


class CalculatorModel:
    def __init__(self):
        self.valeur = ""

    
    def add(self, op):
        if self.valeur == "" and op in "+-×÷()":
            self.valeur = ""
            return self.valeur
        elif len(self.valeur)>=1 and self.valeur[-1].isdigit() and op =="(":
            self.valeur += "×" + op
            return self.valeur
        elif self.valeur == "" and op == "+/-":
            self.valeur = "-"
            return self.valeur
        elif self.valeur == self.valeur and op == "+/-":
            self.valeur = "-" + self.valeur
            return self.valeur
        

        elif len(self.valeur)>=1 and self.valeur[-1] in "+-×÷√" and op in "+-×÷√":
            self.valeur = self.valeur
            return self.valeur
        
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
        

    
    