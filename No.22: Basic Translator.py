def tanslate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        elif letter in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation

print(tanslate(input("Enter a phrase: ")))