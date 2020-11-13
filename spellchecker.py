"""
(c) Gubareve
Created 15-Mar-20
"""
try:
    from similar import findsimilar

    print()
    print("Welcome to the KD7T Spellcheker")
    print()
    import json

    top = 0
    bot = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def convert(lst):  # just stuff cause json sucks
        return lst[0].split()

    with open("dict.json", "r") as f:
        jsontext = json.load(f)
    words = jsontext
    print()
    print("Enter the text you want to spellcheck:")
    textstring = input(">> ")
    print()
    print()
    textarray = eval('["' + textstring + '"]')
    textwords = convert(textarray)

    def capital(string):
        capitalarray = []
        capitalarray.append(string)
        firstletter = capitalarray[0][0]
        if firstletter.isupper():
            return True
        else:
            return False

    def ends(string):
        endsarray = []
        endsarray.append(string)
        lastletter = endsarray[0][-1]
        if (
            lastletter == "."
            or lastletter == ","
            or lastletter == "?"
            or lastletter == "!"
        ):
            return True
        else:
            return False

    for word in textwords:
        if word in words:
            # Spelled correctly
            print("Good Word    --------> " + word)
            top += 1
            bot += 1
        elif capital(word):
            # Is correct
            print("Capital Word --------> " + word)
            top += 1
            bot += 1
        elif ends(word):
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace("?", "")
            word = word.replace("!", "")
            if word in words:
                print("Good Word    --------> " + word)
                top += 1
            else:
                tryword = findsimilar(word)
                for singletryword in tryword:
                    if singletryword in words:
                        print(word + " --------> " + singletryword)
            bot += 1
        else:
            # Bad Word, Reccomend
            bot += 1
            tryword = findsimilar(word)
            for singletryword in tryword:
                if singletryword in words:
                    print(word + " --------> " + singletryword)
    print()
    print()
    percent = top / bot
    percent = percent * 100
    percent = int(percent)
    print("#########################")
    print("##       RESULTS        ")
    print("##  %" + str(percent) + " Correct")
    print("#########################")
except Exception as e:
    print()
    print()
    print(f"Sorry, a Error Happened {e}")
