import customtkinter 

class CalculatorView():
    def __init__(self, root):
        self.root = root

        #display
        self.root = customtkinter.CTk()
        self.root.title("Calculator2026")
        self.root.iconbitmap("OIP.ico")
        self.root.minsize(480, 540)
        self.root.resizable(True, True)
        self.root.geometry("480x540")
        self.root.config(bg="#1e1e1e")

        self.create_frame()    
    
        #stocker texte ecran
        self.display_var = customtkinter.StringVar()
        
        self.create_display()
        self.create_buttons()

   

    
    def create_frame(self):
        self.frame = customtkinter.CTkFrame(self.root, bg_color= "#000000")
        self.frame.pack(fill="both", expand=True)

    def create_display(self):
        display_entry = customtkinter.CTkEntry(self.frame, textvariable=self.display_var, font=("Arial", 24), border_width= 10, insertwidth=2, width=14, justify='right')
        display_entry.grid(row= 0, column=0, columnspan=4, sticky="nsew")
       
    def create_buttons(self):
        button_texts = [
            'AC', '√', '⇐', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '()', '0', '.', '='
        ]

        row_val = 1
        col_val = 0

        for text in button_texts:
            button = customtkinter.CTkButton(self.frame, text=text, bg_color="#075DA8", font=("Arial", 18), command=lambda t=text: self.controller.on_button_click(t), width=60, height=60)
            button.grid(row=row_val, column=col_val, sticky="nsew")
            
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
    



