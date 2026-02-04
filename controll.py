class CalculatorControll :
    def __init__(self, model, view):
        self.model = model()
        self.view = view(self)
        self.view.controller = self
        
        

    def on_button_click(self, char):
        
        current_text = self.view.get_display()

        if char == 'AC':
            # Effacer ecran
            self.view.set_display("")
        elif char == '=':
            # Lancer le calcul
            result = self.model.calculate(current_text)
            self.view.set_display(result)
        elif char == '⇐':
            # supprimer le dernier caractere
             self.view.set_display(current_text[:-1])
        else:
           
            if current_text == "Erreur":
                self.view.set_display(char)
            else:
                self.view.set_display(current_text + char)




