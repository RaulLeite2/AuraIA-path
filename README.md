# Maze Navigation AI

## Description

This project aims to solve the classic maze navigation problem using the **Breadth-First Search (BFS)** algorithm. The goal is to find the shortest path between a start point and an end point in a maze represented as a matrix.

## Features

- **16x16 Maze**: The maze is represented by a matrix where `0` indicates a free path and `1` represents a wall. The start point and the end point are defined as `(start)` and `(goal)`, respectively.
- **Breadth-First Search (BFS)**: The BFS algorithm is used to explore the maze and find the shortest path from the start point to the end point.
- **Visualization**: The project includes a graphical interface to visualize the maze and the path found by the AI. Walls, paths, and the found path are displayed in a graphical representation.

## Project Structure

1. **Maze Definition**:
   - The maze matrix is initialized with values representing paths and walls.
   - The start and end points are specified.

2. **AI Implementation**:
   - The `is_valid` function checks if a position is valid for exploration (within maze limits and not a wall).
   - The `find_path` function uses the BFS algorithm to find the shortest path from the start point to the end point.

3. **Graphical Interface**:
   - The maze and the found path are visualized using the `matplotlib` library. Walls are shown in one color, the found path in another, and the start and end points are highlighted.

## How to Run

1. **Requirements**:
   - `numpy`: Library for array manipulation.
   - `matplotlib`: Library for graphical visualization.

2. **Execution**:
   - Run the Python script to initialize the maze and visualize the results.

## Examples

- **Sample Maze**: A 16x16 maze with the start point `(15, 0)` and the end point `(15, 14)`.
- **Path Found**: The shortest path found by the AI is displayed in the graphical interface.

## Contributing

Feel free to contribute improvements or suggestions. If you encounter any issues or have any questions, please open an issue in the repository.
