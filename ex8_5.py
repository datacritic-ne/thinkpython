def rotate_word(word, b):

    new_word = ''

    for i in range(len(word)):
        char = word[i]

        if (char.isupper()): # encoding upper-case characters
            new_word += chr((ord(char) + b-65) % 26 + 65)
        else:
            new_word += chr((ord(char) + b-97) % 26 + 97)

    return new_word

print(rotate_word('trouble', 6))
