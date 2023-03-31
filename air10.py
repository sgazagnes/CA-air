import sys

def check_nb_arg(args, nb_required):
    return len(args) == nb_required

if(not check_nb_arg(sys.argv[1:], 1)):
    print('Error')
    sys.exit()

filename = sys.argv[1]
try:
    f = open(filename, 'r')
except Exception:
    print('Cannot open the file')
    exit()

print(f.read(), end='')
f.close()
