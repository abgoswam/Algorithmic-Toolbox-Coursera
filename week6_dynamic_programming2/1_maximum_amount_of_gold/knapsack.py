# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    # print(w)
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result

    n = len(w)
    f = np.zeros((n+1, W+1))

    for i in range(1, n+1):
        for _weight in range(1, W+1):

            v1 = 0
            w_i = w[i-1]  # match indices of numpy array and list w
            if _weight - w_i >= 0:
                v1 = f[i-1, _weight - w_i] + w_i

            v2 = f[i-1, _weight]
            f[i, _weight] = max(v1, v2)

    return int(f[n, W])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
