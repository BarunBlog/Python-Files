# Shortest path of a night in a chess board from source to destination
front = 0
rear = 0
queue = [ 0 for i in range(64) ]

def enqueue(node):
    global front
    queue[front] = node
    front = front + 1

def dequeue():
    global rear
    temp = queue[rear]
    rear = rear + 1
    return temp

def adjacency(chess_board):
    adj = [[0 for col in range(64)] for row in range(64)]

    for i in range(8):
        for j in range(8):
            a = chess_board[i][j]
            if i-1>=0 and j-2>=0:
                b = chess_board[i-1][j-2]
                adj[a][b] = 1
                adj[b][a] = 1
            if i+1<=7 and j-2>=0:
                b = chess_board[i+1][j-2]
                adj[a][b] = 1
                adj[b][a] = 1
            if i-2>=0 and j-1>=0:
                b = chess_board[i-2][j-1]
                adj[a][b] = 1
                adj[b][a] = 1
            if i+2<=7 and j-1>=0:
                b = chess_board[i+2][j-1]
                adj[a][b] = 1
                adj[b][a] = 1
            if i-2>=0 and j+1<=7:
                b = chess_board[i-2][j+1]
                adj[a][b] = 1
                adj[b][a] = 1
            if i+2<=7 and j+1<=7:
                b = chess_board[i+2][j+1]
                adj[a][b] = 1
                adj[b][a] = 1
            if i-1>=0 and j+2<=7:
                b = chess_board[i-1][j+2]
                adj[a][b] = 1
                adj[b][a] = 1
            if i+1<=7 and j+2<=7:
                b = chess_board[i+1][j+2]
                adj[a][b] = 1
                adj[b][a] = 1
    return adj

def bfs(src, dest):
    chess_board = []
    k = 0
    for i in range(8):
        li = []
        for j in range(8):
            li.append(k)
            k = k + 1
        chess_board.append(li)

    adj = adjacency(chess_board)
    visited = [0 for i in range(64)]
    level = [0 for i in range(64)]

    enqueue(src)
    visited[src] = 1

    while front != rear:
        square = dequeue()
        for i in range(64):
            if adj[square][i] == 1 and visited[i] == 0:
                enqueue(i)
                visited[i] = 1
                level[i] = level[square] + 1

    return level[dest]

src = int(input('Enter the Source: '))
dest = int(input('Enter the Destination: '))
print("Shortest path is: ",bfs(src, dest))
