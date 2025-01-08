i = 0
n = int(input("Enter the number of queens: "))
array = [-1] * n

def is_safe(array, i, j):
    for k in range(i):
        if array[k] == j or abs(array[k] - j) == abs(k - i):
            return False
    return True

while i < n:
    placed = False
    for j in range(array[i] + 1, n):
        if is_safe(array, i, j):
            array[i] = j
            placed = True
            break
    if placed:
        i += 1
    else:
        array[i] = -1
        i -= 1
        if i < 0:
            print("No solution found.")
            break

if i == n:
    board = [["⬜" for _ in range(n)] for _ in range(n)]
    for y in range(n):
        board[y][array[y]] = "🔴"

    for row in board:
        print(" ".join(row))