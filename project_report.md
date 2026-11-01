# Project Report — Campus Navigator

## Problem Statement
Finding routes between campus buildings can be difficult for new students and visitors. This project provides a simple way to explore campus connections.

## Implementation
Campus locations are represented as vertices, and connections between them are represented as edges. An adjacency list stores these connections.

## Working
- The user selects an option from the menu.
- BFS searches for the shortest route between two locations.
- DFS explores locations connected to a starting point.
- The system identifies disconnected locations and handles invalid inputs.

## Complexity
Both BFS and DFS have a time complexity of **O(V + E)**, where V represents vertices and E represents edges.

## Limitations
The project uses predefined campus connections and does not calculate actual walking distances or travel times.

## Future Scope
The project can be extended by adding real campus maps, distance-based routes, and a graphical interface.

## Conclusion
The project demonstrates how graph algorithms can solve a basic navigation problem using Python.
