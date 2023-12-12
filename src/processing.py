import re
from typing import List, Dict, Tuple

def get_text_with_blanks(text: str, frequency: int, ratio: float = 0.5) -> Tuple[str, Dict[int, str]]:
    '''
    Returns the text with blanks and a dictionary of answers.
    
    Parameters:
        text (str): The base text.
        frequency (int): The number of words every two blanks.
        ratio (float): The ratio of the word to be shown. 1 means the whole word is shown, 0 means only one letter of the word is shown.
    '''
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio must be between 0 and 1")
    
    new_text = ''
    current_word = ''
    awaiting_char = '' 

    word_count = 0
    blank_count = 0
    answers = {}

    text_length = len(text)

    if ratio == 1:
        return text, answers

    for i, char in enumerate(text):
        if char in (" ", "\n", "\t") or i == text_length - 1:

            word_count += 1

            if current_word != '':
                word_length = len(current_word)
                next_char = awaiting_char if awaiting_char != '' else ' '
                shown_chars = int(word_length * ratio) if word_length * ratio >= 1 else 1
                new_text += current_word[:shown_chars] + '_' * (word_length - shown_chars) + '(' + str(blank_count) + ')' + next_char
                answers[blank_count] = current_word[shown_chars:]
                blank_count += 1
                awaiting_char = ''

            else:
                new_text += ' '
            
            current_word = ''

        if word_count % frequency == 0:

            if re.match(r'\b\w+\b', char):
                current_word += char
            
            elif current_word != '':
                awaiting_char = char

            else:
                new_text += char

        else:
            new_text += char
        

    return new_text, answers




