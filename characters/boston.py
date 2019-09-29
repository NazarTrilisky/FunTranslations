import re
from random import randint


# text combinations to replace
replace_dict = {
    '([\w]{2,})er(\W)': r'\1ah\2',
    '([\w]{2,})er': r'\1ah',
    '(\w)ers(\W)': r'\1ahs\2',
    '(\w)ar(\W)': r'\1ah\2',
    '(\W)your(\W)': r'\1yah\2',
    'you ': "ya ",
    '(\w)eir(\w)': r'\1eei\2',
    '(\w)off(\w)': r'\1ahf\2',
    '(\w)on(\w)': r'\1aw\2',
    '(\w)ard': r'\1ahd'
    
}

def get_intro():
    """ return an introductory exclamation """
    rand_num = randint(0,5)
    if 0 == rand_num:
        return "Go Sox! "
    elif 1 == rand_num:
        return "Go Bruins! "
    elif 2 == rand_num:
        return "Go Pats! "
    elif 3 == rand_num:
        return "Go Celtics! "
    elif 4 == rand_num:
        return "Wicked! "
    elif 5 == rand_num:
        return "Pissa! "
    else:
        raise Exception("Unexpected num!")


def boston_talk(in_txt):
    """ return the in_txt as a new englander would say it """
    for key in replace_dict.keys():
        in_txt = re.sub(key, replace_dict[key], in_txt, re.IGNORECASE)
    return get_intro() + in_txt

