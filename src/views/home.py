from tkinter import ttk
from .generics import BaseView

class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "CONTROLE DE DESLIGAMENTO DO PC")

        ttk.Label(self, text="Escolha uma opção:").pack(pady=10)

        ttk.Button(self, text="Timer", command=lambda: controller.show_view("TimerView")).pack(pady=10, padx=5)
        ttk.Button(self, text="Data e Hora", command=lambda: controller.show_view("DateTimeView")).pack(pady=10, padx=5)
