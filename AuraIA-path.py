import numpy
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Matriz que define o Maze Map
maze = numpy.array([
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 3, 0]
])

# Posições de entrada, saída, parede e caminho
start = (15, 0)
goal = (15, 14)
path_value = 0
wall = 1

def is_valid(maze, pos):
    """Verifica se a posição está dentro dos limites da matriz e não é uma parede."""
    x, y = pos
    return (0 <= x < maze.shape[0] and
            0 <= y < maze.shape[1] and
            maze[x, y] != wall)

def find_path(maze, start, goal):
    """Encontra o caminho do início ao objetivo no labirinto usando BFS."""
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if is_valid(maze, neighbor) and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    # Reconstrução do Caminho
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = came_from.get(step)
    path.reverse()
    return path

def plot_maze(maze, path=None): # (opicional)
    """Plota o labirinto e o caminho encontrado."""
    cmap = mcolors.ListedColormap(['white', 'black', 'blue', 'red'])
    bounds = [0, 1, 2, 3]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    cax = ax.imshow(maze, cmap=cmap, norm=norm)

    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, path_x, color='yellow', marker='o', linestyle='-', markersize=8, linewidth=2)

    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

# Encontrar o caminho
path_found = find_path(maze, start, goal)
print(f"Caminho encontrado: {path_found}")

# Plotar o labirinto e o caminho
plot_maze(maze, path_found)
