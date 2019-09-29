import re
from random import randint


# text combinations to replace
replace_dict = {
    ' the ': " thuh ",
    '(\W)I(\W)': r'\1I totally\2',
    '(\W)You(\W)': r'\1you totally\2',
    '(\W)he(\W)': r'\1he totally\2',
    '(\W)she(\W)': r'\1she totally\2',
    '(\W)it(\W)': r'\1it totally\2',
    '(\W)they(\W)': r'\1they totally\2',
    '(\W)we(\W)': r'\1we totally\2',
    
    'I(\W)': r'I totally\1',
    'You(\W)': r'you totally\1',
    'he(\W)': r'he totally\1',
    'she(\W)': r'she totally\1',
    'it(\W)': r'it totally\1',
    'they(\W)': r'they totally\1',
    'we(\W)': r'we totally\1',
}

def get_intro():
    """ return an introductory exclamation """
    rand_num = randint(0,2)
    if 0 == rand_num:
        return "Yeah, so like ... "
    elif 1 == rand_num:
        return "So like you know ... "
    elif 2 == rand_num:
        return "Ugh!  WhatEVER! ... "
    else:
        raise Exception("Unexpected Num!")
        

def valley_girl_talk(in_txt):
    """ return the in_txt as a pirate would say it """
    for key in replace_dict.keys():
        in_txt = re.sub(key, replace_dict[key], in_txt, re.IGNORECASE)
    return get_intro() + in_txt

