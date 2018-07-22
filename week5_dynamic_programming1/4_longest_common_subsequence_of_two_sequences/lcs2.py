#Uses python3

import sys
import numpy as np

def lcs2(a, b):
    #write your code here

    n = len(a)
    m = len(b)

    lcs = np.zeros((n+1, m+1), np.int32)

    for i in range(1, n+1):
        for j in range(1, m+1):
            v = [lcs[i, j-1], lcs[i-1, j]]
            if a[i-1] == b[j-1]:
                v.append(lcs[i-1, j-1] + 1)
            else:
                v.append(lcs[i-1, j-1])

            lcs[i, j] = max(v)

    return lcs[n, m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
