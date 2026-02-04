from tkinter import*
from controll import CalculatorControll
from model import CalculatorModel
from view import CalculatorView



if __name__ == "__main__":
    app = CalculatorControll(CalculatorModel, CalculatorView)
    app = app.view.get_root()
    app.mainloop()