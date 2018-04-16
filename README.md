# Man's Labyrinth
CMPUT275 Final Project
By Songhui Zhang (1499982), James Hryniw (1431912)

Uses [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
to generate 3D mazes.

#### Overview:
* The maze automatically generates upon running `main.py`.
* The dimensions of the maze can be adjusted by clicking the dimension then entering a number. Note: There are soft limits.
* Each layer of the maze is connected vertically by green/red ladders, representing a path to a higher/lower layer.
* The player is a blue square, and the exit is a door at the bottom-right corner of the highest layer.
* There is a lower generation 'weight' for paths between layers, i.e. verticality is reduced compared to a purely-kruskal's maze.
* The maze is represented by an undirected graph, and a wall represent the lack of a path between adjacent nodes.
* Techniques used in the project:
  * Kruskal's algorithm
  * Binary heap
  * Breadth-first search
  * Union find

#### Controls:
* `WASD` For horizontal movement.
* `QE` For vertical movement (up/down green/red ladders respectively).
* `up/dn` To peek between layers.
* `P` To view the solution.

#### Requirements:
* Python 3
* pygame (`sudo pip3 install pygame`)
* To run, navigate to project directory and enter `python3 main.py`
