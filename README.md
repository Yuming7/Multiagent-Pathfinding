# Multiagent-Pathfinding

Overview
This Python code implements a grid-based pathfinding algorithm using the A* search algorithm and the Conflict-Based Search (CBS) algorithm for multi-agent pathfinding. The code is organized into several classes, each serving a specific purpose in solving pathfinding problems on a 2D grid.

Classes
State
Represents a state in grid-based pathfinding.
Contains coordinates (x, y), cost values (g, cost), and methods for comparison and hashing.
Implements A* search heuristics.
CBSState
Represents a state in the CBS algorithm for multi-agent pathfinding.
Manages constraints, paths, and costs for multiple agents.
Computes the cost of a CBS state and checks for conflicts.
Generates successors with constraints.
CBS
Implements the CBS algorithm for multi-agent pathfinding.
Utilizes a priority queue for state exploration.
Searches for a solution by iteratively expanding states and handling conflicts.
AStar
Implements the A* search algorithm for single-agent pathfinding.
Uses a priority queue to explore states based on their cost.
Computes the cost of nodes and recovers the solution path.
How to Use
Create a grid map and define start and goal positions for agents.
Instantiate a CBSState with the map, starts, and goals.
Use the CBS class to perform the CBS search.
If a solution is found, retrieve paths and costs.
