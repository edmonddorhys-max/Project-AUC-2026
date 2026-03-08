import math


class CalculatorModel:
    def __init__(self):
        self.valeur = ""
        self.history = []
 
    
    def add(self, op):
        if self.valeur == "" and op in "+-×÷()%":
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
        self.history.append(f"{self.valeur} = {result}")
        self.valeur = result
        return result
     except Exception:
        return "Erreur"

    def check_parity(self):
        try:
            expression = self.valeur.replace('÷', '/').replace('×', '*').replace('^', '**').replace('%', '/100')
            val = eval(expression)
            
            if float(val).is_integer():
                if int(val) % 2 == 0:
                    result = "Pair"
                else:
                    result = "Impair"
            else:
                result = "Erreur"
            
            self.history.append(f"Mod({self.valeur}) = {result}")
            self.valeur = result
            return result
        except Exception:
            return "Erreur"

    def calculate(self):
        try:
            result = str(eval(self.valeur.replace('÷', '/').replace('×', '*').replace('^', '**').replace('%', '/100').replace('Mod', '%'))) 
            self.history.append(f"{self.valeur} = {result}")
            return result
        except Exception:
            return "Erreur"
    
        

    
    