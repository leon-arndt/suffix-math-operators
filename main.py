# Calculate an expression using suffix notation, eg: 1 3 * -1 / 4 +

def calc():
    raw_input = input('Enter operators and operands separated by a space: ')
    split_input = str.split(raw_input)
    result = evaluate(split_input)[0]
    print(f'Result is: {result}')


def evaluate(param_list):
    print(param_list)

    operators = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: y - x,
        '/': lambda x, y: y / x,
    }

    last_operator = param_list.pop()
    if last_operator not in operators:
        param_list.append(last_operator)
        return param_list

    param_list = evaluate(param_list)
    operand_1 = int(param_list.pop())

    param_list = evaluate(param_list)
    operand_2 = int(param_list.pop())

    # evaluate and recurse
    result = operators[last_operator](operand_1, operand_2)
    param_list.append(result)

    return param_list


if __name__ == '__main__':
    calc()
