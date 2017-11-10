# Created by: Kay Lin
# Created on: 10th-Nov-2017
# Created for: ICS3U
# This program displays check if two strings are identical
# ignore capticals and smalls

def check_if_true(string_1, string_2):
    # enter two strings and check if they are identical
    # converts both to uppercase
    
    string_1 = string1.upper()
    string_2 = string2.upper()
    
    if string_1 == string_2:
        return True
    else:
        return False
    
string1 = raw_input('Enter string: ')
string2 = raw_input('Enter next string: ' )
string_print = check_if_true(string1, string2)
print(string_print)
