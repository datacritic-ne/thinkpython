#! python3

# loop, every number from 100000 to 999999
# num 1: last 4 digits are palindromic
# num 2 = num 1 + 1, last 5 digits are palindromic
# num 3 = num 2 + 1, digits 2-5 are palindromic
# num 4 = num 3 + 1, all 6 digits are palindromic

for i in range (100000, 999999):
    num_str = str(i)
    num_str_1 = str(i+1)
    num_str_2 = str(i+2)
    num_str_3 = str(i+3)
    if ((num_str[2] == num_str[5]) and (num_str[3] == num_str[4]) and 
        (num_str_1[1] == num_str_1[5]) and (num_str_1[2] == num_str_1[4]) and
        (num_str_2[1] == num_str_2[4]) and (num_str_2[2] == num_str_2[3]) and
        (num_str_3[0] == num_str_3[5]) and (num_str_3[1] == num_str_3[4]) and
        (num_str_3[2] == num_str_3[3])):
        print(i)
    else:
        continue
    
