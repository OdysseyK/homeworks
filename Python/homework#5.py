            # Find All Numbers Disappeared in an Array

def findDisappearedNumbers(nums):
    st = set(nums)
    return set(range(1, len(nums) + 1)) - st

n = [4,3,2,7,8,2,3,1]
assert findDisappearedNumbers(n) == {5, 6}


            # Keyboard Row

def findWords(words):
    patterns = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    answer = []
    for x in words:
        k = x.lower()
        for i in patterns:
            if all(j in i for j in k):
                answer.append(x)
    return answer


n = ["Hello","Alaska","Dad","Peace"]
assert findWords(n) == ['Alaska', 'Dad']


            # Transpose

def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

n = [[1,2,3],[4,5,6],[7,8,9]]
assert transpose(n) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


            # Reshape Matrix

def flat(nested_list):
    c = []
    for i in nested_list:
        if type(i) == list:
            c.extend(flat(i))
        else:
            c.append(i)
    return c

def matrixReshape(mat, r, c):
    if r*c > len(mat)*len(mat[0]):
        r, c = len(mat), len(mat[0])
    tmp = flat(mat)
    return [[tmp.pop(0) for _ in range(c)] for _ in range(r)]


mat = [[1,2],[3,4]]
r = 4
c = 1
assert matrixReshape(mat, r, c) == [[1], [2], [3], [4]]


            #Battleships

def countBattleships(board):
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                if i <= len(board) - 2 and board[i + 1][j] != 'X' and j <= len(board[0]) - 2 and board[i][j + 1] != 'X':
                    ans += 1
                if i == len(board) - 1 and j <= len(board[0]) - 2 and board[i][j + 1] != 'X':
                    ans += 1
                if j == len(board[0]) - 1 and i <= len(board) - 2 and board[i + 1][j] != 'X':
                    ans += 1
                if i == len(board) - 1 and j == len(board[0]) - 1:
                    ans += 1

    return ans


mat = [["X",".",".","X"],[".",".","X","."],[".","X",".","."],[".",".",".","."],[".",".","X","."],[".",".",".","X"]]
assert countBattleships(mat) == 6
