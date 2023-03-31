import sys
import time

def check_all_args_int(args):
    all_digits = 0
    for arg in args:
        if arg.isdigit():
            all_digits+=1
    return all_digits == len(args)

def check_nb_arg(args, nb_required):
    return len(args) >= nb_required


def quick_sort_partition(nb_list, partition_idx):
    lo, hi, pivot_idx = partition_idx
    pivot = nb_list[pivot_idx]
    while(True):
        while(lo <= len(nb_list)-1 and nb_list[lo] < pivot):
            lo+=1

        while(nb_list[hi] > pivot and hi > 0):
            hi-=1

        if(lo >= hi):
            nb_list[pivot_idx] = nb_list[lo]
            nb_list[lo] = pivot
            break

        switch = nb_list[lo]
        nb_list[lo] = nb_list[hi]
        nb_list[hi] = switch

    return lo


arguments = sys.argv[1:]
if(not check_nb_arg(arguments, 3) or not check_all_args_int(arguments)):
    print('Error')
    exit()

numbers = [int(x) for x in arguments]
lo = 0
hi = len(numbers) - 2
pivot_idx = len(numbers) - 1
partition_idx = [[lo, hi, pivot_idx]]

while(len(partition_idx) > 0):
    pivot_idx = quick_sort_partition(numbers, partition_idx[0])
    lo_left = partition_idx[0][0]
    hi_left = pivot_idx-2
    if(hi_left >= lo_left):
        partition_idx.append([lo_left, hi_left, hi_left+1])
    lo_right = pivot_idx+1
    hi_right = partition_idx[0][1]
    if(lo_right <= hi_right):
        partition_idx.append([lo_right, hi_right, hi_right+1])

    partition_idx.pop(0)

print(*numbers)
