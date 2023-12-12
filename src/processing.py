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


text = '''Inß recent years, the integration of artificial intelligence (AI) into healthcare systems has sparked significant transformations, revolutionizing the medical field. AI's unparalleled capacity to analyze vast amounts of data and recognize patterns has led to breakthroughs in disease diagnosis, personalized treatment plans, and drug discovery.

Advanced AI algorithms can identify subtle anomalies in medical images like MRIs and CT scans, enhancing early detection of diseases such as cancer. Additionally, AI-driven predictive modeling assists clinicians in foreseeing potential health risks in patients, enabling proactive interventions. Drug development has also benefited, with AI-driven simulations expediting the identification of potential drug candidates and their interactions.'''

print(get_text_with_blanks(text, 5, 0.3))




''' Kept just in case

def get_sanitized_words(text: str) -> List[str]:

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = text.lower()
    return text.split()


def get_half_word_dict(words: List[str], frequency: int) -> Tuple[Dict[str, str], Dict[int, str]]:

    half_word_dict = {}
    answers = {}
    indices = (frequency * i for i in range(len(words) // frequency))
    j = 0
    for i in indices:
        word = words[i]
        if word not in half_word_dict:
            word_len = len(word)
            half_word = word[:word_len // 2] + '_' * (word_len - word_len // 2) + '(' + str(j) +')'
            half_word_dict[word] = half_word
            answers[j] = word[word_len // 2:]
            j += 1

    return half_word_dict, answers
    

def replace_into_text(text, half_word_dict):
    
    for word, half_word in half_word_dict.items():
        text = re.sub(r'\b' + re.escape(word) + r'\b', half_word, text)
    return text


'''
