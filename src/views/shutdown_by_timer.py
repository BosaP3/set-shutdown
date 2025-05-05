from tkinter import ttk, messagebox
import tkinter as tk
import datetime

from .generics import BaseView
from src.utils.shutdown import schedule_shutdown_in, abort_shutdown

class TimerView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Desligar por Temporizador")

        self.hours_var = tk.StringVar(value="0")
        self.minutes_var = tk.StringVar(value="30")

        frame_timer = ttk.Frame(self)
        frame_timer.pack(pady=10)

        ttk.Label(frame_timer, text="Horas:").pack(side="left", padx=(0, 5))
        ttk.Entry(frame_timer, width=5, textvariable=self.hours_var).pack(side="left", padx=(0, 15))

        ttk.Label(frame_timer, text="Minutos:").pack(side="left", padx=(0, 5))
        ttk.Entry(frame_timer, width=5, textvariable=self.minutes_var).pack(side="left")

        self.create_button_row([
            ("Voltar", lambda: controller.show_view("HomeView")),
            ("Confirmar", self.confirm),
            ("Cancelar Desligamento", self.cancel_shutdown)
        ])

    def confirm(self):
        try:
            hours = int(self.hours_var.get())
            minutes = int(self.minutes_var.get())

            if hours < 0 or minutes < 0 or (hours == 0 and minutes == 0):
                messagebox.showerror("Erro", "Informe um tempo válido maior que zero.")
                return

            delta = datetime.timedelta(hours=hours, minutes=minutes)
            seconds = int(delta.total_seconds())
            schedule_shutdown_in(seconds)

            messagebox.showinfo("Desligamento Agendado", f"O sistema será desligado em {hours}h {minutes}min.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao agendar desligamento: {e}")

    def cancel_shutdown(self):
        try:
            abort_shutdown()
            messagebox.showinfo("Cancelado", "O desligamento foi cancelado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cancelar desligamento: {e}")
