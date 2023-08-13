def solve_maze(maze, row, col, dest_row, dest_col):
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == 1:
        return False  # Current cell is out of bounds or a wall

    if row == dest_row and col == dest_col:
        return True  # Destination reached

    # Mark the current cell as visited
    maze[row][col] = 1

    # Explore adjacent cells in all four directions
    if (solve_maze(maze, row - 1, col, dest_row, dest_col) or  # Up
        solve_maze(maze, row + 1, col, dest_row, dest_col) or  # Down
        solve_maze(maze, row, col - 1, dest_row, dest_col) or  # Left
        solve_maze(maze, row, col + 1, dest_row, dest_col)):   # Right
        return True

    # If no path is found from this cell, backtrack
    maze[row][col] = 0
    return False

# Example maze represented by a 2D grid
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start_row, start_col = 0, 0
dest_row, dest_col = 4, 4

if solve_maze(maze, start_row, start_col, dest_row, dest_col):
    print("Path found!")
else:
    print("No path found!")
