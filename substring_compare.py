def remove_specials(strg):
    string_array = list(strg.lower())
    for i in range(len(string_array)):
        if(97 > ord(string_array[i])) or (122 < ord(string_array[i])):
            string_array[i] = ''

    fixed_string = ''.join(string_array)
    return fixed_string

def compare(strg1, strg2):
    if len(strg1) == 0 or len(strg2) == 0:
        return  ''
    fixed_string_1 = remove_specials(strg1)
    fixed_string_2 = remove_specials(strg2)

    longest_same_subtring = ''
    current_substring = ''
    match_pointer = 0
    for k in range(len(fixed_string_2)):
        for i in range(len(fixed_string_1)):
            if fixed_string_1[i] == fixed_string_2[match_pointer]:
                current_substring += fixed_string_2[match_pointer]
                if len(current_substring) > len(longest_same_subtring):
                    longest_same_subtring = current_substring
                if match_pointer < len(fixed_string_2) - 1:
                    match_pointer += 1
                else:
                    break
            else:
                match_pointer = k
                current_substring = ''

    return longest_same_subtring

if __name__ == '__main__':
    text2 = 'cccABBdaaccc!!!'
    text1 = 'asd.adABBaacc?!s'

    sub = compare(text1, text2).upper()
    if len(sub) == 0:
        sub = 'Brak'
    print('Najwikszy wspólny podciąg: ' + sub)