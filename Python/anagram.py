def difference_num_letters(num_letters_string1, num_letters_string2):
    num = 0
    for letter, value in num_letters_string1.items():
        if letter in num_letters_string2:
            num += abs(value - num_letters_string2[letter])
        else:
            num += value
    for letter, value in num_letters_string2.items():
        if letter not in num_letters_string1:
            num += value
    return num


def get_num_letters(string):
    letters = dict()
    for s in string:
        if s in letters:
            letters[s] += 1
        else:
            letters[s] = 1

    print(letters)
    return letters

def get_num_removed_letters(string1, string2):
    num_letters_string1 = get_num_letters(string1)
    num_letters_string2 = get_num_letters(string2)
    return difference_num_letters(num_letters_string1, num_letters_string2)

if __name__ == '__main__':
    string1 = 'hello'
    string2 = 'billion'
    print(get_num_removed_letters(string1, string2))