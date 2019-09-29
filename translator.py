
# This module translates text to the accent / style of the given character

from characters.pirate import pirate_talk
from characters.emoji import emoji_talk
from characters.pig_latin import pig_latin_talk
from characters.boston import boston_talk
from characters.valley_girl import valley_girl_talk
from characters.shakespeare import shakespeare_talk


def translate(character, in_text):
    return_text = ""
    character = character.lower().strip()
    if 'pirate' == character:
        return_text = pirate_talk(in_text)
    elif 'emoji' == character:
        return_text = emoji_talk(in_text)
    elif "pig_latin" == character:
        return_text = pig_latin_talk(in_text)
    elif "boston" == character:
        return_text = boston_talk(in_text)
    elif "valley_girl" == character:
        return_text = valley_girl_talk(in_text)
    elif "shakespeare" == character:
        return_text = shakespeare_talk(in_text)
    else:
        return_text = "Unrecognized character!!!"
    return return_text


if __name__ == '__main__':
    txt = "I went to the stor to buy you milk."
    print(txt)
    print(translate("valley_girl", txt))



