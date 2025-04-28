#! python3

word = input("> ")
string = input("> ")

def uses_only(w, str):
    cond = True
    letters = list(str)
    for letter in letters:
        if letter not in w:
            cond = False
        else:
            continue
    print(cond)

uses_only(word, string)