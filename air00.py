import sys

def check_args_int(args):
    for arg in args:
        if arg.isdigit():
            return True
    return False

def check_nb_arg(args, nb_required):
    return len(args) == nb_required

def cut_string(string, separators):
    min_idx = 0
    tab_with_words = []
    found_sep = True
    for i, char in enumerate(string):
        if(found_sep == True and string[i] not in separators):
            min_idx = i
            found_sep = False
            continue

        elif(found_sep == True):
            continue

        if(char in separators):
            tab_with_words.append(string[min_idx:i])
            found_sep = True

    tab_with_words.append(string[min_idx:])
    return tab_with_words

arguments = sys.argv[1:]
if not check_nb_arg(arguments, 1) or check_args_int(arguments):
    print('Error')
    sys.exit()

message = sys.argv[1]

cutted_message = cut_string(message, [' ', '\n', '\t'])
for elt in cutted_message:
    print(elt)
