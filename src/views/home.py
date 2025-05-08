from tkinter import ttk
from .generics import BaseView

class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "AGENDADOR DE DESLIGAMENTO")  
        
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill='both', padx=40, pady=20)
        
        ttk.Button(
            main_frame,
            text="⏱️ Desligar por Temporizador",
            command=lambda: controller.show_view("TimerView")
        ).pack(fill='x', pady=2, ipady=15, ipadx=20)
        
        ttk.Button(
            main_frame,
            text="📅 Desligar por Data e Hora",
            command=lambda: controller.show_view("DateTimeView")
        ).pack(fill='x', pady=10, ipady=15, ipadx=20) 
        
        ttk.Button(
            main_frame,
            text="Sair",
            command=controller.root.destroy
        ).pack(fill='x', pady=(20, 10), ipady=5)
