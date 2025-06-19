import random
from utils import calculate_total_distance, get_neighbors, generate_initial_solution

def tabu_search(distance_matrix, tenure=10, max_iterations=1000):
    n = len(distance_matrix)
    current_solution = generate_initial_solution(n)
    best_solution = current_solution[:]
    best_cost = calculate_total_distance(best_solution, distance_matrix)

    tabu_list = {}
    iteration = 0

    while iteration < max_iterations:
        neighbors = get_neighbors(current_solution)
        neighbors.sort(key=lambda x: calculate_total_distance(x[0], distance_matrix))

        for neighbor, move in neighbors:
            cost = calculate_total_distance(neighbor, distance_matrix)
            if move not in tabu_list or cost < best_cost:
                current_solution = neighbor
                if cost < best_cost:
                    best_solution = neighbor[:]
                    best_cost = cost
                tabu_list[move] = iteration + tenure
                break

        # Usuwanie przestarzałych ruchów z listy tabu
        expired = [m for m, exp in tabu_list.items() if exp <= iteration]
        for m in expired:
            del tabu_list[m]

        iteration += 1

    return best_solution, best_cost