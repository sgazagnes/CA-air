import sys

def check_all_args_int(args):
    all_digits = 0
    for arg in args:
        if arg.isdigit():
            all_digits+=1
    return all_digits == len(args)

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required


def combine_string(arguments, separator):
    min_idx = 0
    full_message = arguments[0]

    for elt in arguments[1:]:
        full_message += separator + elt
    return full_message

arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 2) or check_all_args_int(arguments)):
    print('Error')
    exit()

separator = arguments[-1]

message = combine_string(arguments[:-1],separator)
print(message)
