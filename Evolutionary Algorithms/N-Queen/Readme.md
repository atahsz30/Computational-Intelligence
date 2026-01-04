
# N-Queens Problem using Genetic Algorithm

This project implements a **Genetic Algorithm (GA)** solution for the **N-Queens problem** in C++.  
The program searches for **fundamental (unique) solutions** while eliminating symmetric duplicates using rotation and reflection.

---

## 🧠 Problem Description

The **N-Queens problem** requires placing `Q` queens on an `N × N` chessboard such that no two queens attack each other:
- No shared rows
- No shared columns
- No shared diagonals

In this implementation:
- `N = Q = 9`
- The goal is to discover a predefined number of **fundamental solutions** (default: 46).

---

## ⚙️ Algorithm Overview

This solution uses a **Genetic Algorithm** with the following components:

### Representation
- Each chromosome represents a board configuration.
- A chromosome consists of `Q` queen coordinates `(row, column)`.
- Each column contains exactly one queen.

### Fitness Function
- Fitness is defined as the **number of conflicts** between queens.
- A fitness value of `0` indicates a valid solution.

### Genetic Operators
- **Selection**: Tournament selection (k = 5)
- **Crossover**: Column-preserving crossover between two parents
- **Mutation**: Random row reassignment for a queen
- **Elitism**: Best individuals are preserved across generations

### Symmetry Reduction
To avoid counting duplicate solutions:
- All rotations (90°, 180°, 270°)
- Reflections
are generated and stored.
Only **fundamental solutions** are kept.

---

## 📌 Parameters (Configurable)

```cpp
int n = 9;              // Board size
int q = 9;              // Number of queens
int fundNum = 46;       // Number of fundamental solutions to find
int populationNum = 30; // Population size

double elitismRate = 0.1;
double mutationRate = 0.8;
```
## An Example for n = 8, q = 8:
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|   Q  .  .  .  .  .  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  .  .  .  .  Q  .  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  
|   .  .  .  .  .  .  Q  .  .   |  .  .  .  Q  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  
|   .  .  .  Q  .  .  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  Q  .  .  .   |  
|   .  .  .  .  .  .  .  Q  .   |  .  .  .  .  .  .  .  .  Q   |  .  .  .  .  .  .  .  .  Q   |  .  .  Q  .  .  .  .  .  .   |  
|   .  .  Q  .  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  Q  .  .  .  .  .  .  .  .   |  
|   .  .  .  .  .  .  .  .  Q   |  .  .  .  .  .  Q  .  .  .   |  .  .  .  Q  .  .  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  
|   .  .  .  .  .  Q  .  .  .   |  Q  .  .  .  .  .  .  .  .   |  Q  .  .  .  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  
|   .  Q  .  .  .  .  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  .  .  .  .  .  .  .  .  Q   |  
|   .  .  .  .  Q  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  .  .  .  Q  .  .  .  .  .   |  
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|   .  .  .  Q  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  
|   Q  .  .  .  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  Q  .  .  .  .  .  .  .  .   |  
|   .  .  .  .  Q  .  .  .  .   |  .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  .  .  .  .  .  .  .  Q  .   |  
|   .  Q  .  .  .  .  .  .  .   |  Q  .  .  .  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  .  .  .  Q  .  .  .  .  .   |  
|   .  .  .  .  .  .  .  .  Q   |  .  .  Q  .  .  .  .  .  .   |  .  .  .  .  .  .  .  .  Q   |  .  .  .  .  .  .  .  .  Q   |  
|   .  .  .  .  .  .  Q  .  .   |  .  .  .  .  .  .  Q  .  .   |  .  .  .  .  .  .  Q  .  .   |  .  .  .  .  .  .  Q  .  .   |  
|   .  .  Q  .  .  .  .  .  .   |  .  .  .  .  .  .  .  .  Q   |  Q  .  .  .  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  
|   .  .  .  .  .  .  .  Q  .   |  .  .  .  Q  .  .  .  .  .   |  .  .  .  Q  .  .  .  .  .   |  .  Q  .  .  .  .  .  .  .   |  
|   .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  Q  .  .  .   |  
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|   .  .  .  .  .  .  Q  .  .   |  .  .  Q  .  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  .  .  .  Q  .  .  .  .  .   |  
|   .  .  .  Q  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  .  .  .  .  .  Q  .  .  .   |  
|   Q  .  .  .  .  .  .  .  .   |  .  .  .  .  .  .  .  .  Q   |  .  .  .  .  .  Q  .  .  .   |  .  .  Q  .  .  .  .  .  .   |  
|   .  .  .  .  .  .  .  .  Q   |  .  .  .  Q  .  .  .  .  .   |  .  .  .  .  .  .  .  .  Q   |  .  .  .  .  .  .  .  .  Q   |  
|   .  Q  .  .  .  .  .  .  .   |  Q  .  .  .  .  .  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  .  Q  .  .  .  .  .  .  .   |  
|   .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  .  Q  .  .  .  .  .  .  .   |  .  .  .  .  Q  .  .  .  .   |  
|   .  .  .  .  .  .  .  Q  .   |  .  Q  .  .  .  .  .  .  .   |  .  .  .  Q  .  .  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  
|   .  .  Q  .  .  .  .  .  .   |  .  .  .  .  .  Q  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  Q  .  .  .  .  .  .  .  .   |  
|   .  .  .  .  Q  .  .  .  .   |  .  .  .  .  .  .  .  Q  .   |  Q  .  .  .  .  .  .  .  .   |  .  .  .  .  .  .  Q  .  .   |  
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 


