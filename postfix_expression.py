def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def postfix_expr(expression):
    list_expr = expression.split()
    stack = []
    for item in list_expr:
        if is_number(item):
            stack.append(int(item))
        elif item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '-':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(operand_2 - operand_1)
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
        elif item == '/':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(operand_2 // operand_1)
        else:
            raise ValueError("Недійсний вираз")
    if len(stack) == 1:
        return int(stack[0])
    else:
        raise ValueError("Недійсний вираз")


if __name__ == '__main__':
    str = '-3 24 -25 57 -81 -8 / -28 -7 38 -74 * / * - + * / *'
    print(postfix_expr(str))
