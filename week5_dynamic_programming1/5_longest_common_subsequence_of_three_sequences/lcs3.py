#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    #write your code here

    n = len(a)
    m = len(b)
    l = len(c)

    lcs = np.zeros((n+1, m+1, l+1), np.int32)

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                v = [
                    lcs[i, j, k-1],
                    lcs[i, j-1, k],
                ]

                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    v.append(lcs[i-1, j-1, k-1] + 1)
                else:
                    v.append(lcs[i-1, j-1, k-1])

                lcs[i, j, k] = max(v)

    return lcs[n, m]

    return min(len(a), len(b), len(c))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
