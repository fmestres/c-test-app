from typing import Protocol, List


class Language(Protocol):

    name: str
    language_text: str
    confirmation_text: str
    yes_text: str
    no_text: str
    submit_text: str
    restart_text: str
    show_answers_text: str
    score_text: str
    next_text: str
    special_characters: List[str]