# source: https://unicode.org/emoji/charts/emoji-list.html

import json


with open('./characters/emoji_dict.json', 'r') as fh:
    emoji_dict = json.load(fh)  # key = keyword like "smile", value = HTML hex for the emoji
  

def emoji_talk(in_txt):
    """ return in_txt in emoji lingo """
    new_words = []
    for word in in_txt.split():
        if word.lower() in emoji_dict.keys():
            new_words.append(emoji_dict[word.lower()])
        else:
            new_words.append(word)
    
    return ' '.join(new_words)
