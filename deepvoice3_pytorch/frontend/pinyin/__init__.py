# coding: utf-8
from deepvoice3_pytorch.frontend.text.symbols import symbols
n_vocab = len(symbols) + 5

def text_to_sequence(text, p=0.0):
    from deepvoice3_pytorch.frontend.text import text_to_sequence
    text = text_to_sequence(text, ["transliteration_cleaners"])
    return text

from deepvoice3_pytorch.frontend.text import sequence_to_text
