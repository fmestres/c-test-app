from lang_data import *
from typing import List
from protocols import Language
import requests


# fetch most common words from the corpus of the language
def fetch_essential_words(language: Language, frequency: int) -> List[str]:
    lang_corpus = requests.get(language.corpus_url)