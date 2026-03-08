import customtkinter as ctk




class CalculatorView():
    def __init__(self, root):
        self.root = root

        #display
        self.root = ctk.CTk()
        self.root.title("LightGroup-Calculator2026")
        self.root.iconbitmap("calculator.ico")
        self.root.minsize(530, 540)
        self.root.resizable(False, False)
        self.root.geometry("380x650")
        self.root.configure(fg_color="#1e1e1e")
      
     
        # Container pour la calculatrice (gauche)
        self.calc_container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.calc_container.pack(side="left", fill="both", expand=True)
        self.history_visible = False

        self.create_top_bar()
           
    
        #stocker texte ecran
        
        self.display_var = ctk.StringVar(value="0")

        self.create_display()
        self.create_frame() 
        self.create_buttons()
    
    def create_top_bar(self):
        self.top_bar = ctk.CTkFrame(self.calc_container, fg_color="transparent")
        self.top_bar.pack(fill="x", padx=10, pady=(5, 0))
        
        self.btn_quit = ctk.CTkButton(
            self.top_bar, 
            text="Power", 
            width=60, 
            height=25,
            fg_color="#FF0000", 
            hover_color="#D58181",
            command=lambda: self.controller.close_app()
        )
        self.btn_quit.pack(side="left")

    def create_frame(self):
        self.buttons_frame = ctk.CTkFrame(self.calc_container, fg_color="transparent")
        self.buttons_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # On configure 4 colonnes et 5 lignes de taille egale
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
    

    def create_display(self):




        self.display_entry = ctk.CTkEntry(
        self.calc_container, 
        textvariable=self.display_var, 
        font=("Roboto", 50), 
        border_width=0, 
        fg_color="transparent", 
        text_color="white",
        justify='right',
        height=150)
        self.display_entry.pack(fill="x", padx=20, pady=(20, 0))
        self.display_entry.configure(state="readonly")

    
        
       
    def create_buttons(self):
        button_texts = [
            
            ['AC', '()', '%', '⌫'],
            ['√', 'Mod', '🕒', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]
        dark_grey = "#1C1C1C"  # Pour les chiffres
        light_grey = "#333333" # Pour les operateur
        orange = "#FF9F0A"     # Pour le bouton égal 
        cyan_text = "#0FEDE6"  # Pour le texte "AC"
        btn_size = 75
        
        btn_radius = btn_size / 2
        
        padding_val = 8 

        

        for row_idx, row in enumerate(button_texts):
            for col_idx, text in enumerate(row):
                
                bg_color = dark_grey
                txt_color = "white"
                hover_col = "#2C2C2C"

                if text in ['÷', '×', '-', '+', '√', 'Mod', '%', '()']:
                    bg_color = light_grey
                    hover_col = "#444444"
                elif text == '=':
                    bg_color = orange
                    hover_col = "#E08B00"
                elif text == 'AC':
                    bg_color = light_grey
                    txt_color = cyan_text
                    hover_col = "#444444"
                elif text == '⌫':
                    bg_color = "#FF0000"
                    hover_col = "#D58181"
    
                elif text == "≡":
                    hover_col = "#1e1e1e"
        
                button = ctk.CTkButton(
                    self.buttons_frame,
                    text=text,
                    font=("Roboto", 28, "bold"),
                    fg_color=bg_color,
                    text_color=txt_color,
                    hover_color=hover_col,
                    width=btn_size,
                    height=btn_size,
                    corner_radius=btn_radius,
                    command=lambda t=text: self.controller.on_button_click(t)
                )
                
                button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=padding_val, pady=padding_val)
    
           
    def get_display(self):
        return self.display_var.get()
    
    def set_display(self, value):
        self.display_var.set(str(value))
    
    def get_root(self):
        return self.root
    
    def toggle_menu(self, history):
        if self.history_visible:
            self.history_frame.destroy()
            self.root.geometry("380x650")
            self.history_visible = False
        else:
            self.root.geometry("680x650")
            self.history_frame = ctk.CTkFrame(self.root, fg_color="transparent")
            self.history_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
           

            label_menu = ctk.CTkLabel(self.history_frame, text="🕒", font=("Roboto", 20, "bold"))
            label_menu.pack(pady=(0, 10))

            label = ctk.CTkLabel(self.history_frame, text="Historique", font=("Roboto", 16, "bold"))
            label.pack(pady=(20, 5))

            self.history_textbox = ctk.CTkTextbox(self.history_frame, width=280)
            self.history_textbox.pack(fill="both", expand=True)
            
            
            self.history_visible = True
            self.update_history(history)

    def update_history(self, history):
        if self.history_visible and hasattr(self, 'history_textbox'):
            self.history_textbox.configure(state="normal")
            self.history_textbox.delete("0.0", "end")
            content = "\n".join(reversed(history)) if history else "Aucun historique"
            self.history_textbox.insert("0.0", content)
            self.history_textbox.configure(state="disabled")
