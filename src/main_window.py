import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from typing import Dict
from protocols import Language


class Events:

    combobox_selected = "<<ComboboxSelected>>"
    window_resize = "<Configure>"

class App(tk.Tk):

    def __init__(self, text_with_blanks: str, answers: Dict[int, str], *lang_data: Language):

        super().__init__()

        self.title("C-Test Prep")
        self.inputs = []
        self.text_with_blanks = text_with_blanks
        self.answers = answers
        self.score = None

        self.lang_data = lang_data
        self.cur_lang = 0 # By default, the first language to be passed

#        self.bind(Events.window_resize, self._rerender()) #???
#        self.minsize(600, 400)
        self._make_all()


    def run(self) -> None:

        self.mainloop()


    def _submit(self) -> None:

        correct = 0
        total = 0
        for i, input in enumerate(self.inputs):
            if input.get() != self.answers[i]:
                input.config(bg="pink")
            else:
                input.config(bg="lightgreen")
                correct += 1  
            
            total += 1

        self.score = round(correct / total * 100)

        self._make_score_label(3, 0)


    def _show_answers(self) -> None:

        for i, input in enumerate(self.inputs):
            input.delete(0, tk.END)
            input.insert(0, self.answers[i])
            input.config(state="disabled")


    def _rerender(self):

        for child in self.winfo_children():
            child.destroy()

        self._make_all()


    def _restart(self) -> None:

        self.score = None
        self.inputs = []
        self._rerender()


    def _restart_with_confirmation(self) -> None:
            
            if not askyesno("Restart", self.lang_data[self.cur_lang].confirmation_text):
                return None
    
            self._restart()


    def _change_language(self, event) -> None:

        combobox = event.widget
                    
        if not askyesno("Restart", self.lang_data[self.cur_lang].confirmation_text):
            combobox.current(self.cur_lang)
            return None

        lang = combobox.get()

        for i, lang_data in enumerate(self.lang_data):
            if lang_data.name == lang:
                self.cur_lang = i
                break

        combobox.current(self.cur_lang)

        self._restart()


    def _insert_special_character(self, char_to_insert: str):
        '''Inserts a special character into the currently selected input field.'''
        input = self.focus_get()

        if isinstance(input, tk.Entry):
            input.insert(tk.END, char_to_insert)


    def _make_header(self, row: int, column: int) -> None:

        header_frame = tk.Frame(self)
        header_frame.config(padx=20, pady=10)
        header_frame.grid(row=row, column=column, columnspan=2, sticky="w")

        header = tk.Label(header_frame, text="C-Test")
        header.grid(row=0, column=0, sticky="w")

        lang_label = tk.Label(header_frame, text=self.lang_data[self.cur_lang].language_text)
        lang_label.grid(row=1, column=0, sticky="w")

        lang_options = [lang.name for lang in self.lang_data]
        lang_combobox = ttk.Combobox(header_frame, values=lang_options, state="readonly")
        lang_combobox.grid(row=1, column=1, sticky="w")
        lang_combobox.current(self.cur_lang)
        lang_combobox.bind(Events.combobox_selected, self._change_language)


    def _make_text(self, row: int, column: int) -> None:

        wraplength = max(self.winfo_width() // 2, 300) # TODO: Fix this
        text_frame = tk.Frame(self)
        text_frame.config(padx=20, pady=10)
        text_frame.grid(row=row, column=column, sticky="w")
        text = tk.Label(text_frame, text=self.text_with_blanks, wraplength=wraplength, justify="left")
        text.grid(column=0, rowspan=2, sticky="w")


    def _make_inputs(self, row: int, column: int) -> None:
            
        input_frame = tk.Frame(self)
        input_frame.config(padx=20, pady=10)
        input_frame.grid(row=row, column=column, sticky="w")
        for i in self.answers.keys():
            label = tk.Label(input_frame, text=f"{i}")
            label.grid(row=i, column=1, sticky="w")
            input = tk.Entry(input_frame)
            input.grid(row=i, column=2, sticky="w")
            self.inputs.append(input)


    def _make_buttons(self, row: int, column: int) -> None:
        
        button_frame = tk.Frame(self)
        button_frame.config(padx=20, pady=10)
        button_frame.grid(row=row, column=column, sticky="w")

        submit_button = tk.Button(button_frame, text=self.lang_data[self.cur_lang].submit_text, command=self._submit)
        submit_button.grid(row=0, column=0)

        restart_button = tk.Button(button_frame, text=self.lang_data[self.cur_lang].restart_text, command=self._restart_with_confirmation)
        restart_button.grid(row=0, column=1)

        show_answers_button = tk.Button(button_frame, text=self.lang_data[self.cur_lang].show_answers_text, command=self._show_answers)
        show_answers_button.grid(row=0, column=2)

    
    def _make_special_keys(self, row: int, column: int):

        special_characters = self.lang_data[self.cur_lang].special_characters
        special_keys_frame = tk.Frame(self)
        special_keys_frame.config(padx=20, pady=10)
        special_keys_frame.grid(row=row, column=column, sticky="w")

        for i, char in enumerate(special_characters):
            special_key = tk.Button(special_keys_frame, text=char, command=lambda char_to_insert=char: self._insert_special_character(char_to_insert))
            special_key.grid(row=i//5, column=i%5)


    def _make_score_label(self, row: int, column: int):

        score_label_frame = tk.Frame(self)
        score_label_frame.config(padx=20, pady=10)
        score_label_frame.grid(row=row, column=column, sticky="w")

        score_label_text = "" if self.score is None else f"{self.lang_data[self.cur_lang].score_text} {self.score}%"
        score_label = tk.Label(score_label_frame, text=score_label_text)
        score_label.grid(row=0, columnspan=2)


    def _make_all(self):
        self._make_header(0, 0)
        self._make_text(1, 0)
        self._make_inputs(1, 1)
        self._make_buttons(2, 0)
        self._make_special_keys(2, 1)
        self._make_score_label(3, 0)


