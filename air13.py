import os
import subprocess


tests = ['"Bonjour les gars"', '"Crevette magique dans la mer des étoiles" "la"', '"je" "teste" "des" "trucs" " "', '1 2 3 4 5 4 3 2 1',\
        '"Hello milady,  bien ou quoi ??"', '1 2 3 4 5 "+2"', '"Michel" "Albert" "Therese", "Benoit" "t"', '10 20 30 40 50 60 70 90 33',\
        '10 20 30 fusion 15 25 35', '"Michel" "Albert" "Therese" "Benoit"', 'a.txt', '0 3', '6 5 4 3 2 1']

expected = ["Bonjour\nles\ngars", "Crevette magique dans \n mer des étoiles", "je teste des trucs", '5' ,\
           "Helo milady, bien ou quoi ?", '3 4 5 6 7', 'Michel' ,'10 20 30 33 40 50 60 70 90', '10 15 20 25 30 35', 'Albert, Therese, Benoit, Michel',\
           'Je suis un chat', '  0  \n 000 \n00000', '1 2 3 4 5 6']

nb_tests = 13
success = 0
fails = 0
for i in range(0,13):
    try:
        response=subprocess.check_output(f'python air{i:02d}.py ', stderr=subprocess.STDOUT,  shell = True)
        proc = subprocess.Popen([f'python air{i:02d}.py {tests[i]}'], stdout=subprocess.PIPE, shell = True, universal_newlines=True)
        (out, err) = proc.communicate()
        if(out[:-1] == expected[i]):
            # print(out[:-1], expected[i])
            success += 1
            print(f'air{i:02d}.py 1/1: success')
        else:
            print(out[:-1], expected[i])

            fails+=1
            print(f'air{i:02d}.py 1/1: Failure')

    except:
       print(f'python air{i:02d}.py does not exist')
       exit()

print(f'Total success = {success} sur {nb_tests}')
