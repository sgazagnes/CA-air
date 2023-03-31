import sys

def check_args(args):
    check_fusion = 'fusion' in args
    all_digits = 0
    for arg in args:
        if arg.isdigit():
            all_digits += 1
    return check_fusion & (all_digits==len(args)-1)

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
if(not check_nb_arg(arguments, 3) or not check_args(arguments)):
    print('Error')
    exit()


for i in range(len(arguments)):
    if(arguments[i] == 'fusion'):
        list1 = [int(x) for x in arguments[:i]]#arguments[:i]
        list2 = [int(x) for x in arguments[i+1:]]#arguments[i+1:]
        if (len(list1) == 0 or len(list2) == 0 or
        not check_if_list_sorted(list1) or
        not check_if_list_sorted(list2)):
            print('Error')
            exit()
        break

for i in range(len(list2)):
    list1 = insert_in_list(list1, list2[i])

print(*list1)
