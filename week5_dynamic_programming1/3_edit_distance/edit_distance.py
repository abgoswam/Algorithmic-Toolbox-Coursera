# Uses python3
import sys
import numpy as np

def edit_distance(s, t):
    #write your code here

    # print(s)
    # print(t)

    N = len(s)
    M = len(t)
    D = np.zeros((N+1, M+1), np.int32)

    for i in range(1, N+1):
        D[i, 0] = i

    for j in range(1, M+1):
        D[0, j] = j

    for i in range(1, N+1):
        for j in range(1, M+1):
            # because of the nature of how this is set up
            # we are actually comparing s(i-1) with d(j-1)
            # for numpy array indices i, j
            if s[i-1] == t[j-1]:
                c1 = D[i-1, j-1]
            else:
                c1 = D[i-1, j-1] + 1

            c2 = D[i, j-1] + 1
            c3 = D[i-1, j] + 1

            D[i, j] = min(c1, c2, c3)

    return D[i, j]


# print(edit_distance('ab', 'a'))

if __name__ == "__main__":
    print(edit_distance(input(), input()))