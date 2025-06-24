import math
import random
from utils import calculate_total_distance, get_random_neighbor, generate_initial_solution, get_neighbors
import matplotlib.pyplot as plt

def simulated_annealing(distance_matrix, initial_temperature=20000, cooling_rate=0.999, min_temperature=1e-5, max_iterations=100000):
    n = len(distance_matrix)
    current_solution = generate_initial_solution(n)
    best_solution = current_solution[:]
    current_cost = calculate_total_distance(current_solution, distance_matrix)
    best_cost = current_cost

    temperature = initial_temperature
    iteration = 0
    cost_history = [current_cost]

    while temperature > min_temperature and iteration < max_iterations:
        neighbor = get_random_neighbor(current_solution)
        neighbor_cost = calculate_total_distance(neighbor, distance_matrix)

        delta = neighbor_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_solution = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        cost_history.append(current_cost)
        temperature *= cooling_rate
        iteration += 1

    plt.plot(cost_history)
    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.title('Zmiana kosztu w trakcie symulowanego wyżarzania')
    plt.grid(True)

    return best_solution, best_cost

