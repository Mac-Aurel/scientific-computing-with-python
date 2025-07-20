def check_each_operations(ope):
    first, second = [], []
    iterator, result = 0, 0
    operator = ''
    ope = ope.translate(str.maketrans({' ': ''}))

    for i in ope:
        iterator += 1
        if not i.isnumeric():
            if i == '+' or i == '-':
                operator = i
                second = ''.join(ope[iterator::])
                first = ''.join(first)
                break
            else:
                return "Error: Operator must be '+' or '-'."
        else:
            first += i
    if operator != '' and first.isnumeric() and second.isnumeric():
        return {'first': [first],
        'second': [second],
        'operator': [operator], 
        'result': [int(first)+int(second)] 
        if operator == '+' 
        else [int(first)-int(second)]} if len(str(first)) < 5\
         and len(str(second)) < 5 else "Error: Numbers cannot be more than four digits."
    else:
        return "Error: Numbers must only contain digits."

def print_operation(operations, option=False):
    if type(operations) is dict:
        first_line, second_line, third_line, result_line = '', '', '', ''
        it = 0
        for first, second, op, result in zip(
        operations['first'], operations['second'], 
        operations['operator'], operations['result']):
            it +=1
            if (len(first) > len(second)) or (len(first) == len(second)):
                first_line += '  ' + first + '    ' if it != len(operations['first'])\
                 else '  ' + first
                second_line += op + ' ' + (' ' * (len(first) - len(second))) + second + '    '\
                 if it != len(operations['first'])\
                  else op + ' ' + (' ' * (len(first) - len(second))) + second
                third_line += '--' + '-'*len(first) + '    '\
                 if it != len(operations['first'])\
                 else '--' + '-'*len(first)
                result_line += ' ' * ((len(first) + 2) - len(str(result))) + str(result) + '    '\
                if it != len(operations['first'])\
                 else ' ' * ((len(first) + 2) - len(str(result))) + str(result)
            elif (len(first) < len(second)):
                first_line += '  ' + ' '*(len(second) - len(first)) + first + '    '\
                 if it != len(operations['first'])\
                  else '  ' + ' '*(len(second) - len(first)) + first
                second_line += op + ' ' + second + '    '\
                if it != len(operations['first'])\
                else op + ' ' + second
                third_line += '--' + '-'*len(second) + '    '\
                if it != len(operations['first'])\
                else '--' + '-'*len(second)
                result_line += ' ' * (len(second) + 2 - len(str(result))) + str(result) + '    '\
                if it != len(operations['first'])\
                else ' ' * (len(second) + 2 - len(str(result))) + str(result)
        if option:
            return first_line + '\n'+ second_line + '\n'\
             + third_line + '\n' + result_line
        else:
            return first_line + '\n'+ second_line + '\n'\
             + third_line
    else:
        return operations

def check_operator(operations):
    merged_operations = {'first': [],
     'second': [], 'operator': [], 'result': []}
    if len(operations) > 5:
        return ('Error: Too many problems.')
    for op in operations:
        temp = check_each_operations(op)
        if type(temp) is dict:
            merged_operations = {keys: merged_operations[keys] + temp[keys]
            for keys in merged_operations}
        else:
            return temp
    return merged_operations

def arithmetic_arranger(problems, show_answers=False):
    problems = print_operation(check_operator(problems), True) if show_answers\
     else print_operation(check_operator(problems))
    return problems

# run_tests  = arithmetic_arranger(["3801 - 2", "123 + 49"])
# answer = '  3801      123\n-    2    +  49\n------    -----'
# for i,j in zip(run_tests, answer):
#     print('run_tests = ',i if i != '\n' else 'h', '\tanswers=', j if j != '\n' else 'h')
#     if i != j:
#         print('DIFERRENCE')

# print(len(run_tests))
# print(len(answer))
