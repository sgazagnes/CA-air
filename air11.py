import sys

def check_arg_int(arg):
    return arg.isdigit()


def check_nb_arg(args, nb_required):
    return len(args) == nb_required



arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 2) or not check_arg_int(arguments[-1])
or len(arguments[0])>1):
    print('Error')
    exit()

n_etages = int(arguments[-1])
n_character = 2*(n_etages-1)+1
char = arguments[0]
for i in range(n_etages):
    for j in range(n_character):
        if(int(n_character/2) - i <= j <= int(n_character/2) + i):
            print(char, end='')
        else:
            print(' ', end='')
    print()
