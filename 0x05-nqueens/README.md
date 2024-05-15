# N Queens Backtracking Algorithm

[task](https://drive.google.com/file/d/1zGXOOEpAEkvtcGDBoMKzERD2WDEPFyQG/view?usp=drive_link)

[backtracking](https://www.geeksforgeeks.org/introduction-to-backtracking-data-structure-and-algorithm-tutorials/)

This Python script solves the N Queens problem using a backtracking algorithm. The N Queens problem is a classic problem in combinatorial optimization and computer science. The objective is to place N chess queens on an N×N chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

## How the Algorithm Works

1. **Initialization**: The algorithm starts by initializing an empty N×N chessboard. Each cell of the board is represented by `-1`, indicating that it is unoccupied.
  
2. **Backtracking**: The algorithm recursively tries to place queens on the board, row by row. At each step, it identifies the available positions for placing a queen in the current row. It then selects a position and marks the positions attacked by the queen. If a valid solution is found (i.e., N queens are placed without attacking each other), it is added to the list of solutions. If no solution is found, the algorithm backtracks and explores other possible placements.
  
3. **Marking Attacked Positions**: To efficiently check for attacks, the algorithm marks the positions attacked by each queen placed on the board. It marks positions horizontally, vertically, and diagonally from the queen's position.
  
4. **Recursive Exploration**: The algorithm explores all possible placements of queens by recursively calling itself. It backtracks whenever a placement leads to an invalid configuration.
  

## How to Use

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository or download the script `n_queens.py`.
  
2. Open a terminal or command prompt.
  
3. Navigate to the directory containing `n_queens.py`.
  
4. Run the script with the desired value of N, where N is the size of the chessboard and the number of queens to be placed.
  
  ```
  python n_queens.py N
  ```
  
  Replace `N` with the desired size of the chessboard.
  
5. The script will print all valid solutions for the N Queens problem on an N×N chessboard.
  

### Example

To find solutions for the 8 Queens problem (placing 8 queens on an 8×8 chessboard), run:

```
python 0-nqueens.py 8
```