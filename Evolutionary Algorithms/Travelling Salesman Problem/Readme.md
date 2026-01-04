# Traveling Salesman Problem (TSP) – 51 Cities  
### Genetic Algorithm Implementation in C++

This project implements a **Genetic Algorithm (GA)** to solve the **Traveling Salesman Problem (TSP)** for a dataset of **51 cities**.  
The objective is to find the **shortest possible tour** that visits each city exactly once and returns to the starting city.

---

## 🧠 Problem Description

Given a set of cities with known coordinates, the Traveling Salesman Problem aims to find the minimum-length Hamiltonian cycle.

In this implementation:
- Number of cities: **51**
- Distance metric: **Euclidean distance**
- Solution method: **Genetic Algorithm**

---

## ⚙️ Algorithm Overview

### Representation
- Each chromosome represents a **complete tour**.
- A tour is stored as a permutation of city indices.
- The first city is revisited at the end to complete the cycle.

### Fitness Function
- Fitness is defined as the **total travel distance** of the tour.
- Lower fitness values indicate better solutions.

---

## 🧬 Genetic Operators

### Selection
- **Tournament selection** with `k = 5`
- Parents are chosen based on minimum fitness

### Crossover
- **Ordered crossover (OX)** with a randomly selected interval
- Preserves city order and prevents duplicates

### Mutation
- **Swap mutation**
- Two random cities in the route are swapped
- Applied with high mutation rate to avoid local minima

### Elitism
- Best individual(s) are copied directly to the next generation

---

## 📌 Parameters

```cpp
int cityNum = 51;
int populationSize = 80;
int elitismRate = 1;
double mutationRate = 0.8;

