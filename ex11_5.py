#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

# here is the "rotate_word" code

for i in range(1, 25):
    for word in words:
        new_word = ""
        for j in range(len(word)):
            char = word[j]

            if (char.isupper()):
                new_word += chr((ord(char) + i-65) % 26 + 65)
            else:
                new_word += chr((ord(char) + i-97) % 26 + 97)

        if new_word in words:
            print(f"{word}, {new_word}")
        else:continue

#def rotate_word(word, b):

#    new_word = ''

#    for i in range(len(word)):
#        char = word[i]

#        if (char.isupper()): # encoding upper-case characters
#            new_word += chr((ord(char) + b-65) % 26 + 65)
#        else:
#            new_word += chr((ord(char) + b-97) % 26 + 97)

#    return new_word