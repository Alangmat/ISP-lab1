# 8 вариант
# A = [[0, 1, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 1, 0, 0, 0],
#      [0, 1, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 0, 0, 0, 1, 1, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0, 0],
#      ]

# 5 вариант
# A = [[0, 1, 1, 0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 1, 0, 1, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0, 1],
#      [0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      ]

# 10 вариант
# A = [[0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 0, 1, 1, 1, 0, 0, 1],
#      [0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1],
#      [1, 0, 0, 1, 0, 0, 1, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      ]

# Тестовый вариант с матрицей меньшего размера
# A = [[0, 1, 1, 0],
#      [0, 0, 0, 0],
#      [0, 0, 0, 1],
#      [0, 1, 0, 0]
#      ]

def multiply_matrices(A, B):
    n = len(A) 
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(mtrx):
    header = "  | "
    x = 0
    result = ""
    while (x < len(mtrx)):
        x += 1
        header += str(x) + ' | '
        row = f"{x} | "
        for i in mtrx[x - 1]:
            row += str(i) + " | "
        result += row + "\n"
    result = header + "\n" + result
    print(result)

def inp_out_nodes(mtrx):
    n = len(mtrx)
    inps, outs = [], []
    i, j = 0, 0
    while i < n:
        i += 1
        if sum(mtrx[i-1]) == 0:
            outs.append(i)
    while j < n:
        j += 1
        s = 0
        for r in mtrx:
            s += r[j-1]
        if s == 0:
            inps.append(j)
    return inps, outs

def seq_matrix(mtrx):
    seq = 1
    temp = mtrx
    while True:
        temp = multiply_matrices(mtrx, temp)
        if sum(sum(row) for row in temp) == 0:
            break
        else: seq += 1
    return seq

def tacts_created(mtrx):
    seq = 0
    n = len(mtrx)
    result = [-1]*n
    temp = mtrx
    while (-1) in result:
        if seq != 0:
            temp = multiply_matrices(temp, mtrx)
        inps, outs = inp_out_nodes(temp)
        for i in inps:
            if result[i-1] == -1:
                result[i-1] = seq
        seq += 1
    return result

def tacts_closed(mtrx, tacts, outs):
    n = len(mtrx)
    result = []
    i = 0
    while i < n:
        j = 0
        temp = []
        while j < n:
            temp.append(mtrx[i][j]*tacts[j])
            j += 1
        result.append(max(temp))
        i += 1
    for x in outs:
        result[x-1] = tacts[x-1]
    return result

def tacts_storage(created, closed):
    result = []
    for i in range(len(created)):
        result.append(closed[i] - created[i])
    return result
    
def matrix_paths(mtrx, seq):
    list_matrixs = []
    result = mtrx
    temp = mtrx
    for i in range(1, seq):
        temp = multiply_matrices(mtrx, temp)
        list_matrixs.append(temp)
    for x in list_matrixs:
        result = [[result[i][j] + x[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    return result

A = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        # разбиваем строку по пробелам и преобразуем в числа
        row = list(map(int, line.strip().split()))
        A.append(row)


inps, outs = inp_out_nodes(A)
print(f'Входные узлы {inps}\nВыходные узлы {outs}')
seq = seq_matrix(A)
print(f'Порядок графа: {seq}')
# print_matrix(A)
tactsCreated = tacts_created(A)
print(f'Такты образования:\t{tactsCreated}')
tactsClosed = tacts_closed(A, tactsCreated, outs)
print(f'Такты гашения:\t\t{tactsClosed}')
tactsStorage = tacts_storage(tactsCreated, tactsClosed)
print(f'Такты хранения:\t\t{tactsStorage}')
matrixPaths = matrix_paths(A, seq)
print("Матрица прямых и косвенных связей:")
print_matrix(matrixPaths)

