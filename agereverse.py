#! python3

# i'm 37, Mom is 73
# this has happened 5 times before
# it should happen once more, and one more time if they're lucky
# what is my age now?

# my age < 10, use myage.zfill(2). zfill has to be applied to strings

# create a list of my ages
# create a list of Mom's ages, mine with the digits reversed

import collections

my_ages = []
mom_ages = []
diff_ages = []

for i in range (1, 100):
    age_str = str(i)
    age_str_fill = age_str.zfill(2)
    my_ages.append(age_str_fill)
#print(my_ages)

for j in range(len(my_ages)):
    mom_age = my_ages[j][1]+my_ages[j][0]
    mom_ages.append(mom_age)
#print(mom_ages)

# subtract Mom's age from my age, create a new list of the differences

for k in range(len(my_ages)):
    diff_age = int(mom_ages[k]) - int(my_ages[k])
    diff_ages.append(str(diff_age))
#print(diff_ages)

# counting occurrences of each differences

count_diff = collections.Counter(diff_ages)
#print(count_diff)

index = [i for i, x in enumerate(diff_ages) if x == '18']
if index:
    print(f"Index of 18: {index}")
else:
    print(f"18 not found.")

print(my_ages[56])