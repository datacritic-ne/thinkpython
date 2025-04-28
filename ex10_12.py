#! python3

file1 = open('words.txt', 'r')
data = file1.read()
words = data.split('\n')

for word in words:
    if len(word) % 2 == 0:
        x = word[::2]
        y = "".join(reversed(word[::-2]))
        if ((x in words) and (y in words)):
            print(f"{word} = {x} and {y}")
        else:
            continue
    else:
        x = word[::2]
        yshort = word[:-1]
        y = "".join(reversed(yshort[::-2]))
        if ((x in words) and (y in words)):
            print(f"{word} = {x} and {y}")
        else:
            continue