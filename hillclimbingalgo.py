import random

# Convert chess notation (like a1) to row and column numbers
def cn_to_idx(cn):  # cn = chess notation, idx = index
    col = ord(cn[0].lower()) - ord('a')
    row = int(cn[1]) - 1
    return row, col

# Validate input for A1 to H8
def validate_input(cn):  # cn = chess notation
    if len(cn) == 2 and cn[0].lower() in "abcdefgh" and cn[1] in "12345678":
        return True
    return False

# Count the number of queen conflicts
def count_conf(state):  # state = list of queen positions
    count = 0  # Conflict counter
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Check for conflicts in the same row or diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count

# Perform hill climbing to minimize conflicts
def climb(state, fixed_col):  # state = queen positions, fixed_col = column of fixed queen
    n = len(state)
    current = state[:]
    
    while True:
        current_conf = count_conf(current)
        if current_conf == 0:
            return current  # Found solution with no conflicts
        
        neighbors = []
        
        # Generate neighboring states
        for col in range(n):
            if col == fixed_col:  # Skip fixed queen's column
                continue
            for row in range(n):
                if row != current[col]:
                    neighbor = current[:]
                    neighbor[col] = row
                    neighbors.append((neighbor, count_conf(neighbor)))
        
        # Sort by least conflicts
        neighbors.sort(key=lambda x: x[1])
        
        # Pick best neighbor
        best_neighbor, best_conf = neighbors[0]
        
        if best_conf < current_conf:
            current = best_neighbor
        else:
            return current  # Local maximum reached, return

# Perform random restart hill climbing
def restart_climb(fixed_col, fixed_row, n=8, restarts=100):  # Fixed queen's position
    solutions = set()
    
    for _ in range(restarts):
        state = [random.randint(0, n - 1) for _ in range(n)]
        state[fixed_col] = fixed_row  # Fix the user-defined queen
        
        final_state = climb(state, fixed_col)
        
        if count_conf(final_state) == 0:
            solutions.add(tuple(final_state))  # Store solution
    
    return solutions

# Print the chessboard
def show_board(state):
    n = len(state)
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    for col in range(n):
        row = state[col]
        board[row][col] = 'Q'  # Place queens
    
    for row in reversed(board):  # Print with white side at the bottom
        print(' '.join(row))
    print()

# Main program
def main():
    n = 8  # Number of queens
    
    # Get initial queen position from user and validate it
    while True:
        initial_pos = input("Enter the initial queen position (A1 to H8): ")
        if validate_input(initial_pos):
            break
        else:
            print("Invalid input! Please enter a valid chess position (A1 to H8).")
    
    fixed_row, fixed_col = cn_to_idx(initial_pos)
    
    # Find solutions using random restart hill climbing
    solutions = restart_climb(fixed_col, fixed_row, n, restarts=1000)
    
    print(f"\nFound {len(solutions)} unique solutions.\n")
    
    # Print each solution
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        show_board(solution)

# Run the main function
if __name__ == "__main__":
    main()