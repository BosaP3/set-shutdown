import tkinter as tk
from tkinter import ttk
from .views.home import HomeView
from .views.shutdown_by_timer import TimerView
from .views.shutdown_by_datetime import DateTimeView

class AutoShutdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Set Shutdown ⏱ ")
        
        window_width = 345
        window_height = 300

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

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
