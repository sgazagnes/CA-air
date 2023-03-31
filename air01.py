import sys

def check_args_int(args):
    for arg in args:
        if arg.isdigit():
            return True
    return False


def check_nb_arg(args, nb_required):
    return len(args) == nb_required

def cut_string(string, separator):
    min_idx = 0
    tab_separated = []
    found_sep = True
    i = 0
    while(True):
        # print(char)
        if(found_sep == True and string[i:i+len(separator)] != separator):
            min_idx = i
            i+=1
            found_sep = False
            continue

        elif(found_sep == True):
            i+=len(separator)
            continue

        if(string[i:i+len(separator)] == separator):
            # print(string[min_idx:i])
            tab_separated.append(string[min_idx:i])
            i += len(separator)-1
            found_sep = True

        i += 1
        if(i >= len(string)-1):
            break
    tab_separated.append(string[min_idx:])
    return tab_separated

arguments = sys.argv[1:]
if not check_nb_arg(arguments, 2) or check_args_int(arguments):
    print('Error: Wrong type or number of arguments.')
    sys.exit()

message = sys.argv[1]
separator = sys.argv[2]
cutted_message = cut_string(message,separator)
for elt in cutted_message:
    print(elt)
