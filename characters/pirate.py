import re
from random import randint


# text combinations to replace
replace_dict = {
    'ed ': "'d ",
    'you': 'yee',
    'wow(\W)': r'Shiver me timbers!\1',
    "I can't believe": 'Shiver me timbers!',
    '(\w)ou(\w)': r'\1ooo\2',
    '(\s)the(\s)': r"\1d'rr\2",
    'it is ' : 'tis ',
    "it's" : "tis",
    ' it ' : " 't ",
    'agreement':'Accord',
    'hello':'Ahoy',
    'emergency':'Allhandsondeck',
    'agreed':'Arrr',
    'stop':'Avast',
    'yes':'Aye',
    'prepareforastorm':'Battendownthehatches',
    'thelowestformoflife':'Bilgerat',
    'apersonwhocannotbetrusted':'Blaggard',
    'stolengoods':'Booty',
    'shipprison':'Brig',
    'pirate':'Buccaneer',
    'awhipmadeofknottedrope':'Cat’o’ninetails',
    'acurvedsword':'Cutlass',
    'pirate':'Cutthroat',
    'thebottomofthesea':'DavyJones’Locker',
    'ocean':'Deep',
    'friends':'Hearties',
    'cheat':'Hornswaggle',
    'pirateflag(skullandcrossbones)':'JollyRoger',
    'landspotted':'Landahoy',
    'alanddweller':'Landlubber',
    'leftaloneonadesertedisland':'Marooned',
    'buddy':'Matey',
    'my':'Me',
    'whenthecrewrebels':'Mutiny',
    'oldsilvercoinsfromSpain':'Piecesofeight',
    'robberofthesea':'Pirate',
    'tosteal':'Plunder',
    'aseasonedsailor':'Salt',
    'understand':'Savvy',
    'troublemaker':'Scourge',
    'adiseasefromlackofvitaminC':'Scurvy',
    'sinktheship':'Scuttle',
    'experiencedsailor':'Seadog',
    'sailingwithoutbeingseasick':'Sealegs',
    'headouttosea':'Setsail',
    'seasongs':'Shanty',
    'adyingsailor':'Sharkbait',
    'fellowsailor':'Shipmate',
    'goodcondition':'Shipshape',
    'crikey':'Shivermetimbers',
    'clean':'Swab',
    'pirate':'Swashbuckler',
    'awaytodisposeofenemies':'Walktheplank',
    'raisetheanchor':'Weighanchor'
}

def get_intro():
    """ return an introductory exclamation """
    rand_num = randint(0,3)
    if 0 == rand_num:
        return "Yarrr mateys! "
    elif 1 == rand_num:
        return "Yo-ho-ho! "
    elif 2 == rand_num:
        return "Yee ol' salt. "
    elif 3 == rand_num:
        return "Shiver me timbers! "
    else:
        raise Exception("Unexpected num!")


def pirate_talk(in_txt):
    """ return the in_txt as a pirate would say it """
    for key in replace_dict.keys():
        in_txt = re.sub(key, replace_dict[key], in_txt, re.IGNORECASE)
    return get_intro() + in_txt

