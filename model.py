import math as m


class CalculatorModel:
    def __init__(self):
        pass
        

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
       return a*b

    def div(self, a, b):
        if b==0:
            raise ValueError("Ne peut pas diviser par zero")
        else:
            return a/b
        

    def racine(self, a):
        
        if a < 0:
            raise ValueError("Ne peut pas calculer la racine carrée d'un nombre négatif")
        else:
            return m.sqrt(a)
        
    def exposant(self, a, b):
        return a**b
        
    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        
        except Exception:
            return "Erreur"
