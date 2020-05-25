##################################
##                              ##
##       INVERT RECURSIVE       ##
##                              ##
##################################

def invert_string(string):
    if len(string) <= 1:
        return string
    return invert_string(string[1:]) + string[0]

##################################
##                              ##
##     PALINDROME RECURSIVE     ##
##                              ##
##################################

def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0].lower() == string[len(string)-1].lower():
        return is_palindrome(string[1:-1])
    else:
        return False


##################################
##                              ##
##    PERMUTATION RECURSIVE     ##
##                              ##
##################################

def permutations(string):
    array = []
    permute(string, '', array)
    return array

def permute(string, chosen, array):
    if len(string) == 0:
        array.append(chosen)

    else:
        for i in range(len(string)):
            char = string[i]
            chosen += char
            string = string[:i] + string[i+1:]
            
            permute(string, chosen, array)

            string = string[:i] + char + string[i:]
            chosen = chosen[:-1]



##################################
##                              ##
##            MAIN              ##
##                              ##
##################################

if __name__ == '__main__':
    string = 'Pedro'
    print('Full String  : ' + string)
    print('Inverted     : ' + invert_string(string))
    print('Palindrome   : ' + str(is_palindrome(string)))
    print('Palindrome   : ' + str(permutations(string)))