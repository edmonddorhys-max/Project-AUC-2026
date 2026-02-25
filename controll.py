class CalculatorControll :
    def __init__(self, model, view):
        self.model = model()
        self.view = view(self) 
        self.view.controller = self

    
    def calculate(self):
        result = self.model.calculate()
        self.view.display_var.set(result)
    
    def on_button_click(self, button_text):
        if button_text == "AC":   
            self.model.valeur = ""
            self.view.set_display("")
        elif button_text == "⇐":
            self.model.valeur = self.model.valeur[:-1]
            self.view.set_display(self.model.valeur)
        elif button_text == "=":
            if self.model.valeur.startswith("√"):
                result = self.model.racine()
            else:
                result= self.model.calculate()
            
            self.view.set_display(result)


        elif button_text == "√":
            self.model.add(button_text) 
            self.view.set_display(self.model.valeur)

       
        elif button_text == "()":
            val = str(self.model.valeur)
        
        
            open_count = val.count('(')
            close_count = val.count(')')
        
        
            if open_count > close_count and val and (val[-1].isdigit() or val[-1] == ')'):
                self.model.add(")")
            
            else:
            
                self.model.add("(")
            self.view.set_display(self.model.valeur)


        else:
            value =self.model.add(button_text)
            self.view.set_display(value)