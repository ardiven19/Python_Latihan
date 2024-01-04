maze = [
    [0,0,0,0,1,1],
    [1,0,1,0,1,1],
    [1,1,0,0,0,1],
    [1,1,1,1,0,0]
]
def showmaze (maze):
    for i in maze:
        print(i)
game = True
pos_awlx = 0
pos_awly = 0
while game:
    maze[pos_awly][pos_awlx] = 8
    showmaze(maze)
    break


