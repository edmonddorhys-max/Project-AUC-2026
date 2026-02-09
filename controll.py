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
            self.calculate()

        elif button_text == "√":
            value = self.model.racine()
            self.view.set_display(value)
        else:
            value =self.model.add(button_text)
            self.view.set_display(value)