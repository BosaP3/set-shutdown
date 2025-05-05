import tkinter as tk
from tkinter import ttk
from .views.home import HomeView
from .views.shutdown_by_timer import TimerView
from .views.shutdown_by_datetime import DateTimeView

class AutoShutdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto Shutdown")
        self.root.geometry("395x250")

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.views = {}
        self._setup_views()
        self.show_view("HomeView")

    def _setup_views(self):
        for ViewClass in (HomeView, TimerView, DateTimeView):
            view = ViewClass(self.container, self)
            self.views[ViewClass.__name__] = view
            view.grid(row=0, column=0, sticky="nsew")

    def show_view(self, view_name):
        self.views[view_name].tkraise()

    def run(self):
        self.root.mainloop()
