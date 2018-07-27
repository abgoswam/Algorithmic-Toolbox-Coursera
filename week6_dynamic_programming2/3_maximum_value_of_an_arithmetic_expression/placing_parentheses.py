# Uses python3
import numpy as np


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


# this shouldonly be invoked if j > i
def minmax(i, j, op, M, m):

    # _max = -sys.maxsize-1
    # _min = sys.maxsize

    # special handle so we dont have to deal with max / min sizes
    a = evalt(M[i, i], M[i + 1, j], op[i])
    b = evalt(M[i, i], m[i + 1, j], op[i])
    c = evalt(m[i, i], M[i + 1, j], op[i])
    d = evalt(m[i, i], m[i + 1, j], op[i])
    _min = min(a, b, c, d)
    _max = max(a, b, c, d)

    for k in range(i+1, j):
        a = evalt(M[i, k], M[k + 1, j], op[k])
        b = evalt(M[i, k], m[k + 1, j], op[k])
        c = evalt(m[i, k], M[k + 1, j], op[k])
        d = evalt(m[i, k], m[k + 1, j], op[k])

        _min = min(_min, a, b, c, d)
        _max = max(_max, a, b, c, d)

    M[i, j] = _max
    m[i, j] = _min


def parenthesis(di, op, M, m):
    for i in range(len(di)):
        M[i, i] = di[i]
        m[i, i] = di[i]

    n = len(di)
    for diff in range(1, n):
        for i in range(n - diff):
            j = i + diff
            minmax(i, j, op, M, m)

    return M[0, n-1]


def get_maximum_value(dataset):
    #write your code here
    # print(dataset)

    di = []
    op = []
    for i in range(len(dataset)):
        # print(i, dataset[i])
        if i % 2 == 0:
            di.append(int(dataset[i]))
        else:
            op.append(dataset[i])

    n = len(di)
    M = np.zeros((n, n))
    m = np.zeros((n, n))

    # print(di)
    # print(op)
    v = parenthesis(di, op, M, m)
    return int(v)


if __name__ == "__main__":
    print(get_maximum_value(input()))
