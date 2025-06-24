import sys
from datetime import time

from pandas.core.nanops import disallow

from utils import generate_coordinates, create_distance_matrix
from tabu_search import tabu_search
from or_tools_solver import solve_tsp_with_or_tools
from visualize import plot_solution
import matplotlib.pyplot as plt
from simulated_annealing import simulated_annealing
import time
from simulated_annealing_optimizer import optimize_sa_parameters

def hundred_runs_test(distance_matrix):
    final_tabu_best_cost = sys.maxsize
    final_tabu_best_solution = []
    final_simulated_annealing_best_cost = sys.maxsize
    final_simulated_annealing_best_solution = []

    start = time.perf_counter()
    for i in range(100):
        tabu_best_solution, tabu_best_cost = tabu_search(distance_matrix)
        if tabu_best_cost < final_tabu_best_cost:
            final_tabu_best_cost = tabu_best_cost
            final_tabu_best_solution = tabu_best_solution
    end = time.perf_counter()
    print(f'Tabu search 100 runs took {end-start:.6f} seconds')
    print(f'Best Tabu search solution cost: {final_tabu_best_cost}')

    start = time.perf_counter()
    for i in range(100):
        simulated_annealing_best_solution, simulated_annealing_best_cost = simulated_annealing(distance_matrix)
        if simulated_annealing_best_cost < final_simulated_annealing_best_cost:
            final_simulated_annealing_best_cost = simulated_annealing_best_cost
            final_simulated_annealing_best_solution = simulated_annealing_best_solution
    end = time.perf_counter()
    print(f'Simulated annealing 100 runs took {end - start:.6f} seconds')
    print(f'Best Simulated annealing solution cost: {simulated_annealing_best_cost}')
def main():
    num_cities = 30
    coords = generate_coordinates(num_cities)
    distance_matrix = create_distance_matrix(coords)

    # # Tabu Search
    tabu_best_route, tabu_best_cost = tabu_search(distance_matrix)
    print("Najlepsza trasa (Tabu Search):", tabu_best_route)
    print("Długość trasy:", tabu_best_cost)
    plot_solution(tabu_best_route, coords, title="Tabu Search", position=(50, 100))

    plt.show()
    
    # # Simulated annealing
    simulated_annealing_best_route, simulated_annealing_best_cost = simulated_annealing(distance_matrix)
    print("Najlepsza trasa (Simulated Annealing):", simulated_annealing_best_route)
    print("Długość trasy:", simulated_annealing_best_cost)
    plot_solution(simulated_annealing_best_route, coords, title="Simulated Annealing", position=(50, 600))

    or_tools_route, or_tools_cost = solve_tsp_with_or_tools(distance_matrix)
    if or_tools_route:
        print("OR-Tools:", or_tools_route)
        print("Długość trasy:", or_tools_cost)

        plot_solution(or_tools_route, coords, title="OR-Tools solver", position=(1300, 100), animate=False)
    else:
        print("Nie udało się znaleźć rozwiązania optymalnego.")

    plt.show()



    hundred_runs_test(distance_matrix)

if __name__ == "__main__":
    main()
