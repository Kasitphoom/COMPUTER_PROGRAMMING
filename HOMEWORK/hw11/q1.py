keyword = {
    "be": "b",
    "because": "cuz",
    "see you": "cu",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    'before': "b4",
    "once": "1ce",
    "and": "&",
    "your": "ur",
    "you're": "ur",
    "as far as I know": "afaik",
    "as soon as possible": "asap",
    "at the moment": "atm",
    "be right back": "brb",
    "by the way": "btw",
    "for your information": "fyi",
    "in my humble opinion": "imho",
    "in my opinion": "imo",
    "laugh out loud": "lol",
    "oh my god": "omg",
    "roll on the floor laughing": "rofl",
    "talk to you later": "ttyl"
}

def textese(s):
    for i in s.split():
        if i in keyword:
            s = s.replace(i, keyword[i])
    
    return s

def untextese(s):
    for i in s.split():
        if i in keyword.values():
            s = s.replace(i, list(keyword.keys())[list(keyword.values()).index(i)])
    
    return s

print(textese("I will see you later tomorrow"))
print(untextese("I will c u l8r 2mro"))