# Uses python3
import sys
import itertools
import numpy as np
import random
# from collections import defaultdict

def is_sum_partition(A, S):
    n = len(A)
    F = np.zeros((n+1, S+1))
    # d = defaultdict(lambda: [])
    d = {}
    for i in range(1, n+1):
        for s in range(1, S+1):
            d[i, s] = []
            if F[i-1, s] == 1:
                F[i, s] = 1
                item_lists = d[i-1, s].copy()
                for l in item_lists:
                    d[i, s].append(l.copy())

            if s - A[i - 1] == 0:
                F[i, s] = 1
                d[i, s].append([A[i-1]])
            elif s - A[i-1] > 0 and F[i-1, s - A[i-1]] == 1:
                F[i, s] = 1
                item_lists = d[i-1, s - A[i-1]].copy()
                for l in item_lists:
                    l.append(A[i-1])
                    d[i, s].append(l.copy())

            # print("{0} -- {1} -- {2} -- {3} -- {4}".format(i, s , A[:i], F[i,s], d[i, s]))

    return F[n, S], d[n, S]


def partition3(A):
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
    #
    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1
    # print("----------------------")
    # print(A, sum(A))

    sum_total = sum(A)
    if sum_total % 3 != 0:
        return 0

    sum_partition = sum_total // 3
    flag, possible_grps = is_sum_partition(A, sum_partition)
    if flag == 0:
        return 0
    else:
        # print("Possibilities 1")
        # print(possible_grps)
        for pgrp in possible_grps:
            a_temp = A.copy()
            for item in pgrp:
                a_temp.remove(item)

            flag, possible_grps2 = is_sum_partition(a_temp, sum_partition)
            if flag == 0:
                continue
            else:
                # print("Possibilities 2 (for group : {0})".format(pgrp))
                # print(possible_grps2)
                return 1

    return 0


def stress_test():
    while True:
        n = random.randint(1, 20)
        A = random.sample(range(1, 30), n)
        partition3(A)


# # stress_test()
# partition3([5, 2, 3, 5])

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

