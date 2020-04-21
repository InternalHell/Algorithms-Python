import doctest

stack = []


def is_bracket_sequence_correct(x: str):
    '''Проверяет коррекность скобочной последовательности () []'''
    for i in x:
        if i not in '()[]':
            continue
        if i in '([':
            stack.append(i)
        else:
            assert i in ')]', 'Error:\n' + str(i)
            if len(stack) == 0:
                return False
            left = stack.pop()
            assert left in '[(', 'Error2' + str(left)
            if left == '(':
                right = ')'
            if left == '[':
                right = ']'
            if right != i:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    doctest.testmod()
    print(is_bracket_sequence_correct(
        'f((([[[()()()((((()))))[][[]][()((()))]]]])))'))
