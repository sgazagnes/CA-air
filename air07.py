import sys

def check_all_args_int(args):
    all_digits = 0
    for arg in args:
        if arg.isdigit():
            all_digits+=1
    return all_digits == len(args)

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required

def check_if_list_sorted(nb_list):
    return all(nb_list[i] <= nb_list[i+1] for i in range(len(nb_list)-1))

def insert_in_list(nb_list, nb_to_insert):
    index = len(nb_list)
    for i in range(len(nb_list)):
        if nb_to_insert <= nb_list[i]:
            index = i
            break
    nb_list.insert(index, nb_to_insert)
    return nb_list

arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 3) or not check_all_args_int(arguments)
or not check_if_list_sorted(arguments[:-1])):
    print('Error')
    exit()

to_insert = int(arguments[-1])
num_list = [int(x) for x in arguments[:-1]]
good_array = insert_in_list(num_list,to_insert)
print(*good_array)
