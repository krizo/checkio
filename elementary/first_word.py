'''
https://py.checkio.org/mission/first-word/solve/
'''

import re

def first_word(text):
    """
        returns the first word in a given text.
    """
    return re.findall(r"[\w']+", text)[0]
