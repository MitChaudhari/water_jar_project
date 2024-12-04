
# Water Jar Project

A Python program that uses **Breadth-First Search (BFS)** to find the shortest path to balance water jars with a targeted value. This project demonstrates the practical application of graph traversal algorithms in solving real-world problems.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Setup and Execution](#setup-and-execution)
5. [Input Details](#input-details)
6. [Example Output](#example-output)
7. [License](#license)
8. [Credits](#credits)

---

## Introduction
The Water Jar Project simulates a scenario where you have three jars with predefined maximum volumes. The goal is to transfer water between the jars to achieve a specific target volume in any one jar using the shortest sequence of operations. The solution leverages the **Breadth-First Search (BFS)** algorithm to explore possible jar states systematically.

---

## Features
- **Efficient Pathfinding**: Uses BFS to find the shortest sequence of operations to achieve the target.
- **Customizable Input**: Accepts user-defined jar volumes and a target value.
- **Interactive Console Interface**: Guides the user through the setup and displays the solution path.
- **Error Handling**: Validates user inputs to ensure correctness.

---

## How It Works
1. Represents the problem as a graph where:
   - Nodes are states of the jars (e.g., `(jar1, jar2, jar3)`).
   - Edges are valid water transfer operations.
2. Uses BFS to traverse the graph and find the shortest path to the target state.
3. Outputs the sequence of operations required to achieve the target or indicates if it's impossible.

---

## Setup and Execution

### Prerequisites
- Python 3.6 or higher.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/MitChaudhari/water_jar_project.git
   cd WaterJarProject/app
   ```
2. Run the program:
   ```bash
   python WaterJar.py
   ```

---

## Input Details
The program will prompt for:
1. The maximum volume of three jars (`jar1`, `jar2`, and `jar3`).
   - Accepted range: 1 to 9.
2. The target volume to achieve.
   - Must be between 1 and the maximum capacity of any jar.

### Example Input
```
Please enter first jar volume between 1 to 9: 3
Please enter second jar volume between 1 to 9: 5
Please enter third jar volume between 1 to 9: 7
Enter the target value between (1 - 7) to get a valid output: 4
```

---

## Example Output
The program outputs the sequence of jar states leading to the target:

```
[(0, 0, 0), (3, 0, 0), (0, 3, 0), (0, 0, 3), (3, 3, 0), (0, 6, 0), (0, 0, 6), (3, 0, 6), (3, 5, 0), (0, 5, 4)]
```

If no solution exists:
```
No such series of operations exist, Please try Again.
```

---

## License
This project is licensed under the **Public Domain**. You are free to use, modify, and distribute it as needed.

---

## Credits
- **Author**: Mitansh Chaudhari
- **Outline Provided By**: Prof. Xiaolong Wang  
  Course: CS - Data Structures and Algorithms  
  Date: November 28, 2022
