import sys

def check_nb_arg(args, nb_required):
    return len(args) == nb_required

def check_arg_int(arg):
    return arg[0].isdigit()

argument = sys.argv[1:]

if(not check_nb_arg(argument, 1) or check_arg_int(argument)):
    print('Error')
    exit()

message = argument[0]
corrected_message = message[0]
for i in range(0, len(message)-1):
    if(message[i] != message[i+1]):
        corrected_message += message[i+1]



print(corrected_message)
