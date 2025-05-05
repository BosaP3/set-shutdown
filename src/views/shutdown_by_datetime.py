from tkinter import ttk, messagebox
import tkinter as tk
import datetime

from .generics import BaseView
from src.utils.shutdown import schedule_shutdown_in, abort_shutdown
from src.utils.helpers import parse_datetime_from_input, get_seconds_until

class DateTimeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Desligar por Data e Hora")

        now = datetime.datetime.now()
        self.day_var = tk.StringVar(value=str(now.day).zfill(2))
        self.month_var = tk.StringVar(value=str(now.month).zfill(2))
        self.year_var = tk.StringVar(value=str(now.year))
        self.hour_var = tk.StringVar(value=str(now.hour).zfill(2))
        self.minute_var = tk.StringVar(value=str(now.minute).zfill(2))

        frame_date = ttk.Frame(self)
        frame_date.pack(pady=5)
        ttk.Label(frame_date, text="Data (dd/mm/aaaa):").pack(side="left", padx=(0, 5))
        ttk.Entry(frame_date, width=3, textvariable=self.day_var).pack(side="left")
        ttk.Label(frame_date, text="/").pack(side="left")
        ttk.Entry(frame_date, width=3, textvariable=self.month_var).pack(side="left")
        ttk.Label(frame_date, text="/").pack(side="left")
        ttk.Entry(frame_date, width=5, textvariable=self.year_var).pack(side="left")

        frame_time = ttk.Frame(self)
        frame_time.pack(pady=5)
        ttk.Label(frame_time, text="Hora (hh:mm):").pack(side="left", padx=(0, 5))
        ttk.Entry(frame_time, width=3, textvariable=self.hour_var).pack(side="left")
        ttk.Label(frame_time, text=":").pack(side="left")
        ttk.Entry(frame_time, width=3, textvariable=self.minute_var).pack(side="left")

        self.create_button_row([
            ("Voltar", lambda: controller.show_view("HomeView")),
            ("Confirmar", self.confirm),
            ("Cancelar Desligamento", self.cancel_shutdown)
        ])

    def confirm(self):
        try:
            date_str = f"{self.day_var.get()}/{self.month_var.get()}/{self.year_var.get()}"
            time_str = f"{self.hour_var.get()}:{self.minute_var.get()}"

            target = parse_datetime_from_input(date_str, time_str)
            seconds = get_seconds_until(target)

            if seconds <= 0:
                messagebox.showerror("Erro", "A data/hora deve ser futura.")
                return

            schedule_shutdown_in(seconds)
            messagebox.showinfo("Desligamento Agendado", f"O sistema será desligado às {target.strftime('%H:%M')} em {target.strftime('%d/%m/%Y')}.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao agendar desligamento: {e}")

    def cancel_shutdown(self):
        try:
            abort_shutdown()
            messagebox.showinfo("Cancelado", "O desligamento foi cancelado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cancelar desligamento: {e}")
