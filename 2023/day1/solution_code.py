# import library
import re

# create an empty list to store all the digits
all_line_twoDigit = []

# open the input file
input = open("input.txt", 'r')
#input = open("test_input.txt", 'r')

#############################################################################################
#             Part 1                                                                        #
#############################################################################################

# read through the lines, find all digits, and save the first one and the last combined
#for line in input.readlines():
#    all_line_twoDigit.append(re.findall(r'\d', line)[0]+re.findall(r'\d', line)[-1])

#############################################################################################
#             Part 2                                                                        #
#############################################################################################

# lookup dictionary forward
lookup_dict_f = {"zero": "0", "0": "0", "one": "1", "1": "1", "two": "2", "2": "2", "three": "3", "3": "3", 
               "four": "4", "4": "4", "five": "5", "5": "5", "six": "6", "6": "6", "seven": "7", "7": "7", 
               "eight": "8", "8": "8", "nine": "9", "9": "9",}

# lookup dictionary reverse
lookup_dict_r = {"zero"[::-1]: "0", "0": "0", "one"[::-1]: "1", "1": "1", "two"[::-1]: "2", "2": "2", "three"[::-1]: "3", "3": "3", 
               "four"[::-1]: "4", "4": "4", "five"[::-1]: "5", "5": "5", "six"[::-1]: "6", "6": "6", "seven"[::-1]: "7", "7": "7", 
               "eight"[::-1]: "8", "8": "8", "nine"[::-1]: "9", "9": "9",}

# lookup patterns
pattern_f = '|'.join(k for k in lookup_dict_f)
pattern_r = '|'.join(k for k in lookup_dict_r)

# the reverse scan is for cases like "gfour1rmznkmplqfsevennksglsfdqtwotwonet"
# the correct answer is 41 not 42
for line in input.readlines():
    first_digit = lookup_dict_f[re.findall(pattern_f, line)[0]]
    last_digit = lookup_dict_r[re.findall(pattern_r, line[::-1])[0]]
    all_line_twoDigit.append(first_digit + last_digit)

# print the sum of the combined two digits
print(sum(map(int, all_line_twoDigit)))
