from time import sleep
lines = [line.strip() for line in open("input", "r")]

def is_valid_cell(x, y, N):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    return True

def find_paths_util(maze, source, destination, visited, path, paths):
  """Find paths using Breadth First Search algorith """
  # Done if destination is found
  if source == destination:#(35,51): # d #destination:
    print(len(path)-1)
    paths.append(path[:])  # append copy of current path
    return

  # mark current cell as visited
  N = len(maze)
  x, y = source
  visited[x][y] = True

  # if current cell is a valid and open cell, 
  if is_valid_cell(x, y, N):# and maze[x][y]:
    # Using Breadth First Search on path extension in all direction
    # go right (x, y) --> (x + 1, y)
    if x + 1 < N and (not visited[x + 1][y]) and (maze[x][y] >= maze[x+1][y]-1):
      #print(maze[x][y], maze[x+1][y], maze[x][y] >= maze[x+1][y], path)
      path.append((x + 1, y))
      find_paths_util(maze,(x + 1, y), destination, visited, path, paths)
      path.pop()

    # go left (x, y) --> (x - 1, y)
    if x - 1 >= 0 and (not visited[x - 1][y]) and (maze[x][y] >= maze[x-1][y]-1):
      path.append((x - 1, y))
      find_paths_util(maze, (x - 1, y), destination, visited, path, paths)
      path.pop()

    # go up (x, y) --> (x, y + 1)
    if y + 1 < N and (not visited[x][y + 1]) and (maze[x][y] >= maze[x][y+1]-1):
      path.append((x, y + 1))
      find_paths_util(maze, (x, y + 1), destination, visited, path, paths)
      path.pop()

    # go down (x, y) --> (x, y - 1)
    if y - 1 >= 0 and (not visited[x][y - 1]) and (maze[x][y] >= maze[x][y-1]-1):
      path.append((x, y - 1))
      find_paths_util(maze, (x, y - 1), destination, visited, path, paths)
      path.pop()

    # Unmark current cell as visited
  visited[x][y] = False

  return paths

def find_paths(maze, source, destination):
  """ Sets up and searches for paths"""
  N = len(maze) # size of Maze is N x N

  # 2D matrix to keep track of cells involved in current path
  visited = [[False]*N for _ in range(N)]

  path = [source]
  paths = []
  paths = find_paths_util(maze, source, destination, visited, path, paths)

  return paths

maze = [[ord(l)-97 for l in line] for line in lines]
N = len(maze)

def getorigin(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == -14:
                return (i,j)

def getexit(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == -28:
                return (i,j)

# Start point and destination
source = getorigin(maze)  # top left corner (0,0)
destination = getexit(maze)  # bottom right corner
#destination = (37,51)
maze[source[0]][source[1]] = 0
maze[destination[0]][destination[1]] = 25
print(source, destination)
print(maze[35][51])
print(len(maze), len(maze[0]))
#for line in maze:
#    print(line)
# Find all paths

paths = find_paths(maze, source, destination)

print("Paths with '->' separator between maze cell locations")
for path in paths:
    #print(*path, sep = ' -> ')
    pass
print(min([len(path)-1 for path in paths]))