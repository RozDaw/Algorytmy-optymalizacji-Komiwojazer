from pandas.core.nanops import disallow

from utils import generate_coordinates, create_distance_matrix
from tabu_search import tabu_search
from optimal_solver import solve_tsp_optimal
from visualize import plot_solution
import matplotlib.pyplot as plt
from simulated_annealing import simulated_annealing  # do dodania

def main():
    num_cities = 30
    coords = generate_coordinates(num_cities)
    distance_matrix = create_distance_matrix(coords)

    # # Tabu Search
    tabu_best_route, tabu_best_cost = tabu_search(distance_matrix)
    print("Najlepsza trasa (Tabu Search):", tabu_best_route)
    print("Długość trasy:", tabu_best_cost)
    plot_solution(tabu_best_route, coords, title="Tabu Search", position=(50, 100))

    # # Simulated annealing
    simulated_annealing_best_route, simulated_annealing_best_cost = simulated_annealing(distance_matrix)
    print("Najlepsza trasa (Simulated Annealing):", simulated_annealing_best_route)
    print("Długość trasy:", simulated_annealing_best_cost)
    plot_solution(simulated_annealing_best_route, coords, title="Simulated Annealing", position=(50, 600))

    optimal_route, optimal_cost = solve_tsp_optimal(distance_matrix)
    if optimal_route:
        print("Optymalne rozwiązanie (OR-Tools):", optimal_route)
        print("Długość trasy:", optimal_cost)

        plot_solution(optimal_route, coords, title="Optimal solver", position=(1300, 100), animate=False)
    else:
        print("Nie udało się znaleźć rozwiązania optymalnego.")

    plt.show()

if __name__ == "__main__":
    main()
