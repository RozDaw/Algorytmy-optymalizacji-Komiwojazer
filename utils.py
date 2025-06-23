import numpy as np
import random

def generate_coordinates(n, seed=42):
    np.random.seed(seed)
    return np.random.rand(n, 2) * 100

def create_distance_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = np.linalg.norm(coords[i] - coords[j])
    return matrix

def calculate_total_distance(route, distance_matrix):
    return sum(distance_matrix[route[i], route[(i + 1) % len(route)]] for i in range(len(route)))

def generate_initial_solution(n):
    route = list(range(n))
    random.shuffle(route)
    return route

def get_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((neighbor, (i, j)))
    return neighbors

def get_random_neighbor(solution):
    a, b = random.sample(range(len(solution)), 2)
    neighbor = solution[:]
    neighbor[a], neighbor[b] = neighbor[b], neighbor[a]
    return neighbor
