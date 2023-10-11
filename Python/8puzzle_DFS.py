# The initial and goal states
given = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # Current state of the puzzle
        self.parent = parent  # Parent node
        self.action = action  # Action that led to this state

def givesChildren(node):
    children = []
    blank_row, blank_col = None, None

    for row in range(3):    # Find the position of the blank tile (0)
        for col in range(3):
            if node.state[row][col] == 0:
                blank_row, blank_col = row, col
                break

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # Define possible moves: (row, col) offsets

    for move in moves:
        new_row, new_col = blank_row + move[0], blank_col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in node.state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            action = "Right" if move == (0, 1) else "Down" if move == (1, 0) else "Left" if move == (0, -1) else "Up"
            children.append(Node(new_state, parent=node, action=action))

    return children

def sol_path(node):
    path = []
    while node is not None:
        if node.action:
            path.insert(0, node.action)
        node = node.parent
    return path

def dfs(node, visited):
    visited.add(tuple(map(tuple, node.state)))

    if node.state == goal:
        return node

    children = givesChildren(node)

    for child in children:
        if tuple(map(tuple, child.state)) not in visited:
            result = dfs(child, visited)

            if result:
                return result

    return None  # No solution found

def inversion(initial):
	new_list = [item for sublist in initial for item in sublist]
	inv = 0
	for i in range(0,9):
		for j in range(i+1,9):
			if new_list[j]!= 0 and new_list[i]!=0 and new_list[i] > new_list[j]:
				inv += 1
	return inv


print("No. of inversions: ",inversion(given))

print("Solution Path using DFS:")
if (inversion(given) % 2 == 0):
  visited = set()
  initial_node = Node(given)
  solution_node = dfs(initial_node, visited)
  solution_path = sol_path(solution_node)
  # print("Solution Path:")
  for step, action in enumerate(solution_path, start=1):
      print(f"Step {step}: Move {action}")
else:
    print("No solution found.")
