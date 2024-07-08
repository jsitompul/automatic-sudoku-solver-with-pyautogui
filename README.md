# Sudoku Solver

This project is an automatic Sudoku solver written in Python. It uses the `pyautogui` library to simulate keyboard inputs and solve Sudoku puzzles on any application where you can input numbers using the keyboard. The solver utilizes a backtracking algorithm to fill in the Sudoku grid.

## Features

- **Automatic Input**: Uses `pyautogui` to input the solved Sudoku puzzle into any application.
- **Backtracking Algorithm**: Efficiently solves the Sudoku puzzle using a classic backtracking algorithm.
- **Customizable**: Can be modified to work with various Sudoku grid formats and applications.

## Requirements

- Python 3.x
- `pyautogui` library
- `numpy` library (although not used in the current version)
- `time` library (standard Python library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/sudoku-solver.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sudoku-solver
    ```
3. Install the required libraries:
    ```sh
    pip install pyautogui numpy
    ```

## Usage

1. Run the script:
    ```sh
    python sudoku_solver.py
    ```
2. Input each row of the Sudoku puzzle when prompted. Input rows as a continuous string of numbers (e.g., `530070000`).
3. Once all rows are inputted, the script will solve the puzzle and automatically input the solution using `pyautogui`.

## How It Works

### Inputting the Sudoku Puzzle

The script prompts the user to input each row of the Sudoku puzzle one at a time. Each row is stored in a list, and the entire puzzle is stored as a 2D list called `sudoku`.

### Solving the Sudoku Puzzle

The script uses a backtracking algorithm to solve the puzzle. It checks for valid placements of numbers in empty cells (represented by `0`), and recursively tries to solve the puzzle by placing numbers and backtracking if necessary.

### Outputting the Solution

Once the puzzle is solved, the `print_sudoku` function uses `pyautogui` to simulate keyboard inputs. It inputs the solution into the currently active application window, moving the cursor appropriately after each number.

## Example

Here's an example of how to input a Sudoku puzzle:

Insert row: 530070000

Insert row: 600195000
Insert row: 098000060
Insert row: 800060003
Insert row: 400803001
Insert row: 700020006
Insert row: 060000280
Insert row: 000419005
Insert row: 000080079



The script will then solve the puzzle and input the solution automatically.

## Notes

- Ensure the application where you want to input the solution is active before running the script.
- The script assumes a standard 9x9 Sudoku grid.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

