CONSONANTS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y']

VOWELS = ['A', 'E', 'I', 'O', 'U']

ALPHANUMERIC = CONSONANTS + VOWELS + ['-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def pig_latin_talk(in_txt):
    """ return the in_txt as it sounds in pig latin """
    in_txt = in_txt.strip()
    if not in_txt or len(in_txt) < 3:
        return in_txt
    
    return_words = []
    for word in in_txt.split():
        new_word = word
        if len(word) > 1:
            if word[0].upper() in VOWELS:
                # start with vowel
                new_word = word + 'ay'
            else:
                # start with consonant
                # place all consonants before fist vowel at end and add "ay"
                for indx in range(1, len(word)):
                    if word[indx].upper() in VOWELS:
                        # indx is the index of 1st non-consonant
                        # check if there is punctuation at the end
                        if word[-1].upper() not in ALPHANUMERIC:
                            # punct is the index of the left-most punctuation char
                            punct = len(word) - 1
                            while punct > 0 and word[punct-1].upper() not in ALPHANUMERIC:
                                punct -= 1
                            new_word = word[indx:punct] + word[:indx] + 'ay' + word[punct:]
                        else:
                            new_word = word[indx:] + word[:indx] + 'ay'
                        break
                        
        return_words.append(new_word)
                
    return ' '.join(return_words)
                    