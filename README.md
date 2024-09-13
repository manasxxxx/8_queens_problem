# 8_queens_problem
8-queens problem using the hill climbing algorithm

# HILL CLIMBING ALGORITHM:

Hill climbing is a heuristic search algorithm for mathematical optimization and solving problems. The goal of hill climbing is continuously moving towards a better solution by iteratively improving the current state until no further improvements can be made. The algorithm "climbs" the "hill" of possible solutions by evaluating neighboring solutions and choosing the one that improves the objective or goal, such as minimizing conflicts or maximizing a score.

# Example in the 8-Queens Problem:

In the 8-queens problem, the algorithm starts with a random arrangement of queens on the board. It evaluates the number of queens attacking each other (conflicts) and tries to move queens to minimize conflicts. The process continues until it finds an arrangement where no queens are attacking each other or until it gets stuck in a state where no improvements can be made.

# Initial Understanding and Approach:

We used a hill climbing algorithm for the 8-queens problem since it’s a heuristic search technique. The goal was to place 8 queens on an 8x8 chessboard so that none of them attacked each other. Hill climbing would allow us to iteratively move towards better configurations by reducing the number of queen conflicts until we reached a solution with zero conflicts.

We broke the problem down into smaller steps:

1. Input Handling: We needed to take the initial position of one queen from the user (e.g., d5) and make sure the input was valid (within a1 to h8).
2. State Evaluation: We had to evaluate how many queens were attacking each other at any given time.
3. Hill Climbing Logic: We needed to generate neighboring board configurations and choose the one that reduced the number of conflicts.
4. Random Restarts: Since hill climbing can get stuck in local optima (non-optimal solutions), we added random restarts to improve the chances of finding valid solutions.

# Collaboration and Code Implementation:

1. Input and Chess Notation Conversion:
One of us handled user input by taking the queen’s position in chess notation (like a1 or d5).
We created a function to convert these positions into indices that could be used for calculations. This step was relatively straightforward, but it laid a crucial foundation for processing the user input correctly.

2. State Evaluation (Conflict Calculation):
Another person focused on writing a function to calculate how many queens were in conflict with each other.
We observed that checking for attacks along rows and diagonals was the most challenging part. Once we figured out how to compare row differences and diagonal conflicts, the function worked efficiently.

3. Hill Climbing Algorithm:
We worked together on the main part of the project, the hill climbing function. It involved evaluating neighboring queen placements and moving toward configurations with fewer conflicts.
We quickly noticed that hill climbing often got stuck in local optima. This was an important realization: hill climbing excels at local search, but without random restarts, it can easily settle on suboptimal solutions.
