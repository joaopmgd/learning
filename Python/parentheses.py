def validate_parantheses(string):
    stack = []

    for char in string:
        
        if char == '(' or char == '{' or char == '[':
            stack.append(char)

        else:
            if len(stack) == 0:
                return False

            previous = stack.pop()
            if (char == ')' and  previous != '(') or (char == '}' and  previous != '{') or (char == ']' and  previous != '['):
                return False

    if len(stack) > 0:
        return False
    return True

if __name__ == '__main__':
    strings = [
        ('[]{}()(((()))){}{([])}', True),
        (']{}()]', False),
        ('{}()]', False),
        ('({[([{}])', False)
    ]
    for values in strings:
        print(validate_parantheses(values[0]), values[1])