import tkinter as tk
from tkinter import ttk

class BaseView(ttk.Frame):
    def __init__(self, parent, controller, title=""):
        super().__init__(parent)
        self.controller = controller
        if title:
            label = ttk.Label(self, text=title, font=("Arial", 16))
            label.pack(pady=15)

    def create_labeled_entry(self, label_text, parent):
        frame = ttk.Frame(parent)
        frame.pack(pady=5)
        ttk.Label(frame, text=label_text).pack(side='left', padx=(0, 5))
        entry = ttk.Entry(frame)
        entry.pack(side='left')
        return entry

    def create_button_row(self, buttons):
        frame = ttk.Frame(self)
        frame.pack(pady=15)
        for text, command in buttons:
            ttk.Button(frame, text=text, command=command).pack(side='left', padx=10)
