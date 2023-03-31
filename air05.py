import sys

def check_all_args_int(args):
    all_digits = 0
    for arg in args:
        if arg.isdigit():
            all_digits+=1
    return all_digits == len(args)

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required


arguments = sys.argv[1:]

if(not check_nb_arg(arguments, 2) or not check_all_args_int(arguments[:-1])
 or len(arguments[-1]) < 2 or arguments[-1][0] not in ['+', '-', '/', '*']
 or not arguments[-1][1:].isdigit()):
    print('Error')
    exit()

numbers = [int(x) for x in arguments[:-1]]
operation = arguments[-1][0]
factor = int(arguments[-1][1:])

if(operation[0] == '+'):
    res = [x +factor for x in numbers]
    print(*res)
elif (operation[0] == '-'):
    res = [x -factor for x in numbers]
    print(*res)
elif (operation[0] == '/'):
    res = [x / factor for x in numbers]
    print(*res)
elif (operation[0] == '*'):
    res = [x * factor for x in numbers]
    print(*res)
