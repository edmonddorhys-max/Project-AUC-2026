from tkinter import*

class CalculatorView:
    def __init__(self, root):
        self.root = root

        

        #display
        self.root = Tk()
        self.root.title("Calculator2026")
        self.root.minsize(480, 540)
        self.root.resizable(False, False)
        self.root.geometry("480x540")
        self.root.config(bg="#FFFFFF")

        self.frame()    
    
        #stocker texte ecran
        self.display_var = StringVar()
        
        self.create_display()
        self.create_buttons()
    
    def frame(self):
        self.frame = Frame(self.root, bg= "#FFFFFF")
        self.root.geometry("480x540")
        self.frame.pack(expand=YES)

    def create_display(self):
        display_entry = Entry(self.frame, textvariable=self.display_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        display_entry.grid(row= 0, column=0, columnspan=4, sticky="nsew")
       
    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'AC', '√', '⇐', '**'
        ]

        row_val = 1
        col_val = 0

        for text in button_texts:
            button = Button(self.frame, text=text, bg="#ABFFD9", font=("Arial", 18), command=lambda t=text: self.controller.on_button_click(t), width=10, height=3)
            button.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        for col in range(4):
            self.frame.grid_columnconfigure(col, weight=1)
        for row in range(row_val + 1):
            self.frame.grid_rowconfigure(row, weight=1)


       
           
    def get_display(self):
        return self.display_var.get()
    
    def set_display(self, value):
        self.display_var.set(str(value))
    
    def get_root(self):
        return self.root
    



