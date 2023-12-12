import tkinter as tk
from tkinter import ttk

class Config(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("C-Test Prep")
        self.inputs = []
        self._make_window()


    def run(self):
        self.mainloop()


    def _make_window(self):

        config_frame = ttk.Frame(self)
        config_frame.grid(row=0, column=0, sticky="nsew")
        
        frequency_label = ttk.Label(config_frame, text="Frequency")
        frequency_label.grid(row=0, column=0, sticky="w")

        frequency_input = ttk.Entry(config_frame)
        frequency_input.grid(row=0, column=1, sticky="w")

        ratio_label = ttk.Label(config_frame, text="Ratio")
        ratio_label.grid(row=1, column=0, sticky="w")

        ratio_input = ttk.Entry(config_frame)
        ratio_input.grid(row=1, column=1, sticky="w")

        self.inputs.append(frequency_input)
        self.inputs.append(ratio_input)

        submit_button = ttk.Button(config_frame, text="Submit", command=self.destroy)
        submit_button.grid(row=2, column=0, sticky="w")



        

