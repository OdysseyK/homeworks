import numpy as np

# Convolution


def conv(a, b):
    tmp = []
    for i in range(0, len(a)-len(b)+1):
        for j in range(0, len(a[0])-len(b[0])+1):
            tmp.append((a[i:i+len(b), j:j+len(b[0])] * b).sum())
    return np.array(tmp).reshape([len(a)-len(b)+1, len(a[0])-len(b[0])+1])


# a = np.array([[0, 1, 1, 1, 0, 0, 0],
#               [0, 0, 1, 1, 1, 0, 0],
#               [0, 0, 0, 1, 1, 1, 0],
#               [0, 0, 0, 1, 1, 0, 0],
#               [0, 0, 1, 1, 0, 0, 0],
#               [0, 1, 1, 0, 0, 0, 0],
#               [1, 1, 0, 0, 0, 0, 0]])
# b = np.array([[1, 0, 1],
#               [0, 1, 0],
#               [1, 0, 1]])
#
# print(conv(a, b))


# Rotate the Matrix


def rotate_90_deg(mat):
    for i in range(len(mat)):
        for j in range(i + 1, len(mat[0])):
            mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
        mat[i] = mat[i][::-1]


# m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# rotate_90_deg(m)
# for i in m:
#     print(i)


