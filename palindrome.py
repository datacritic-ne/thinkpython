def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

#word = "cornucopia"
#print(first(word))
#print(last(word))
#print(middle(word))

def is_palindrome(word):

    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

word = "pop"
print(is_palindrome(word))