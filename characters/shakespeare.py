import re
from random import randint


# text combinations to replace
replace_dict = {
    'right away': 'Anon',
    '^does(\W)': r'Dost\1',
    '(\W)does(\W)': r'\1Dost\2',
    '^do(\W)': r'Doth\1',
    '(\W)do(\W)': r'\1Doth\2',
    'before': 'Ere',
    'listen': 'Hark',
    '^here(\W)': r'Hither\1',
    '(\W)here(\W)': r'\1Hither\2',
    'why': 'Wherefore',
    'gladly': 'Fain',
    'it is': "'Tis",
    'it was': "'Twas",
    '^with(\W)': r'With\1',
    '(\W)with(\W)': r'\1With\2',
    ' of ': ' O ',
    ' to ': " 'T ",
    '^man(\W)': r'Sirrah\1',
    'went' : 'goeth',
    '(\W)man(\W)': r'\1Sirrah\2',
    'woman' : 'Mistress',
    'friend': "cousin",
    '^you(\W)': r'Thou\1',
    '(\W)you(\W)': r'\1Thou\2',
    'your' : 'Thy',
    'yours' : 'Thine',
    '(\w+)est(\W)': r' most \1est\2',
    ' most (\w+)' : r"\1'st",
    'yes(\W)' : r'Aye\1',
    'does': 'doth',
    '(\W)that(\W)': r'\1yon\2',
    '(\W)there(\W)': r'\1yonder\2',
    '(\W)would(\W)': r'\1wish\2',
    '(\W)from where(\W)': r'\1whence\2',
    '(\W)have(\W)': r'\1hast\2',
    '(\W)do(\W)': r'\1dost\2',
    '(\W)are(\W)': r'\1art\2'
}

def get_intro():
    """ return an introductory exclamation """
    rand_num = randint(0,2)
    if 0 == rand_num:
        return "Alas! "
    elif 1 == rand_num:
        return "Behold! "
    elif 2 == rand_num:
        return "S'wounds! "
    else:
        raise Exception("Unexpected random num!")


def shakespeare_talk(in_txt):
    """ return the in_txt as Shakespeare would say it """
    for key in replace_dict.keys():
        in_txt = re.sub(key, replace_dict[key], in_txt, re.IGNORECASE)
    return get_intro() + in_txt

