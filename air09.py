import sys

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required

def array_rotation(list_to_rotate):
    return list_to_rotate[1:] + [list_to_rotate[0]]

arguments = sys.argv[1:]
if not check_nb_arg(arguments, 2):
    print('Error: wrong number of arguments')
    sys.exit()

rotated_list = array_rotation(arguments)
print(', '.join(rotated_list))
