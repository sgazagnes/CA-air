import sys

def check_arg_only_int(args):
    for arg in args:
        if arg.isdigit():
            return True
    return False

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required

def find_good_strings(string_array, bad_chaine):
    good_array = []
    for elt in string_array:
        if bad_chaine.casefold() not in elt.casefold():
            good_array.append(elt)
    return good_array


arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 2) or check_arg_only_int(arguments)):
    print('Error')
    exit()

messages = arguments[:-1]
bad_chaine = arguments[-1]
good_message = find_good_strings(messages,bad_chaine)
for elt in good_message:
    print(elt)
