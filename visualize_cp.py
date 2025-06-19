import matplotlib.pyplot as plt
import numpy as np

def plot_routes(distance_matrix, tabu_route, optimal_route=None):
    coords = np.random.rand(len(distance_matrix), 2)

    plt.figure(figsize=(10, 6))
    plt.title("Porównanie tras: Tabu Search vs. Optymalne")

    # Trasa tabu search (na niebiesko)
    for i in range(len(tabu_route) - 1):
        a, b = tabu_route[i], tabu_route[i + 1]
        plt.plot([coords[a][0], coords[b][0]], [coords[a][1], coords[b][1]], 'b-', label='Tabu Search' if i == 0 else "")

    # Trasa optymalna (na czerwono)
    if optimal_route:
        for i in range(len(optimal_route) - 1):
            a, b = optimal_route[i], optimal_route[i + 1]
            plt.plot([coords[a][0], coords[b][0]], [coords[a][1], coords[b][1]], 'r--', label='Optymalna' if i == 0 else "")

    # Punkty miast
    for i, (x, y) in enumerate(coords):
        plt.plot(x, y, 'ko')
        plt.text(x + 0.01, y + 0.01, str(i), fontsize=9)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
