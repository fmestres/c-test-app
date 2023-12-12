from processing import get_text_with_blanks
from main_window import App

from lang_data import *

text = '''In recent years, the integration of artificial intelligence (AI) into healthcare systems has sparked significant transformations, revolutionizing the medical field. AI's unparalleled capacity to analyze vast amounts of data and recognize patterns has led to breakthroughs in disease diagnosis, personalized treatment plans, and drug discovery.

Advanced AI algorithms can identify subtle anomalies in medical images like MRIs and CT scans, enhancing early detection of diseases such as cancer. Additionally, AI-driven predictive modeling assists clinicians in foreseeing potential health risks in patients, enabling proactive interventions. Drug development has also benefited, with AI-driven simulations expediting the identification of potential drug candidates and their interactions.
'''

if __name__ == "__main__":

    result, answers = get_text_with_blanks(text, 10, 0.6)

    languages = (English,
                 Spanish,
                 German,
                 French,
                 Italian)

    app = App(result, answers, *languages)
    app.run()