import sys

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required


arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 3)):
    print('Error')
    sys.exit()

for i, elt in enumerate(arguments):
    copied_args = arguments.copy()
    copied_args.pop(i)
    if(elt not in copied_args):
        print(elt)
        exit()

print('We did not find any single element')
