#! python3

# here is invert_dict() from the text
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def new_invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], key)
    return inverse
    firstfive = dict(list(inverse.items())[:5])
    print(firstfive)

test_dict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro', 'five': 'cinco', 'six': 'seis', 'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve', 'ten': 'diez'}

inverse = invert_dict(test_dict)
firstfive = dict(list(inverse.items())[:5])
print(firstfive)

inverse2 = new_invert_dict(test_dict)
firstfive = dict(list(inverse2.items())[:5])
print(firstfive)
