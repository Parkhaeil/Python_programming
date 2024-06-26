n , m = map(int , input().split())
grid  = [[0] * n for _ in range(m)]

x = y = 0

#chatgpt 코드를 변형시켜 grid를 만들었습니다.

dirx = [1, 0, -1, 0]
diry = [0, 1, 0, -1]
dir_index = 0

for i in range(n*m):
    grid[x][y] = i+1
    nextx = x+dirx[dir_index]
    nexty = y+diry[dir_index]
    if 0 <= nextx < m and 0 <= nexty < n and grid[nextx][nexty] == 0:
        x = nextx
        y = nexty
    else:
        dir_index = (dir_index + 1) % 4
        x += dirx[dir_index]
        y += diry[dir_index]

for _ in range(4):
    user_input = list(map(int, input().split()))
    if len(user_input) == 1 and i < user_input[0]:
        print("0 0")
    elif len(user_input) == 1:
        for j in range(m):
            for z in range(n):
                if grid[j][z] == user_input[0]:
                        print(z+1,j+1)
    else:

         print(grid[user_input[1]-1][user_input[0]-1])
