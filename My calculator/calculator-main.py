from tkinter import*
from controll import CalculatorControll
from model import CalculatorModel
from view import CalculatorView



if __name__ == "__main__":
    app = CalculatorControll(CalculatorModel, CalculatorView)
    app = app.view.get_root()
    app.mainloop()

"""
Les membres du groupe:
1.EDMOND Dorhys H. Kelly
2.Benjamin Roloussande
3.Kelly Gauthier S.
4.Dorval Jane Lauramene
5.Cétoute Nerlande
"""