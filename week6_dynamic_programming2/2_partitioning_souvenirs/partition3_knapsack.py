# Uses python3
import sys
import itertools
import numpy as np
import random
from collections import defaultdict

def optimal_weight(W, w):
    n = len(w)
    f = np.zeros((n+1, W+1))

    d = defaultdict(lambda: [])
    for i in range(1, n+1):
        for _weight in range(1, W+1):

            v1 = 0
            d1 = None
            w_i = w[i-1]  # match indices of numpy array and list w
            if _weight - w_i >= 0:
                v1 = f[i-1, _weight - w_i] + w_i
                items = d[i-1, _weight - w_i].copy()
                items.append(w_i)
                d1 = items

            v2 = f[i-1, _weight]
            d2 = d[i-1, _weight].copy()

            if d1 is None:
                f[i, _weight] = v2
                d[i, _weight] = d2
            else:
                if v1 >= v2:
                    f[i, _weight] = v1
                    d[i, _weight] = d1
                else:
                    f[i, _weight] = v2
                    d[i, _weight] = d2

    return int(f[n, W]), d[n, W]


def partition3_knapsack(A):

    S = sum(A)
    if S % 3 != 0:
        return 0

    W = S // 3

    w_opt, items1 = optimal_weight(W, A)
    if w_opt != W:
        return 0

    for item in items1:
        A.remove(item)

    w_opt, items2 = optimal_weight(W, A)
    if w_opt != W:
        return 0

    for item in items2:
        A.remove(item)

    print(items1)
    print(items2)
    print(A)

    return 1


partition3_knapsack([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *A = list(map(int, input.split()))
#     print(partition3_knapsack(A))

