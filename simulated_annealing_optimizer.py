import random
from simulated_annealing import simulated_annealing
import matplotlib.pyplot as plt
import math

def optimize_sa_parameters(distance_matrix, initial_temp = 10000, cooling_rate = 0.995, iterations = 10000, outer_iterations=50):
    def perturb(param):
        """Modyfikuj parametr o ±0.5%"""
        change = 1 + (random.uniform(-0.05, 0.05))
        return param * change

    current_params = {
        'initial_temp': initial_temp,
        'cooling_rate': cooling_rate,
        'iterations': iterations
    }

    current_solution, current_distance = simulated_annealing(
        distance_matrix=distance_matrix,
        initial_temperature=current_params['initial_temp'],
        cooling_rate=current_params['cooling_rate'],
        max_iterations=int(current_params['iterations'])
    )

    best_params = current_params.copy()
    best_distance = current_distance

    cost_history = [current_distance]
    param_temp = 1000.0

    for _ in range(outer_iterations):
        # Nowe losowo zmodyfikowane parametry
        new_params = {
            'initial_temp': perturb(current_params['initial_temp']),
            'cooling_rate': perturb(current_params['cooling_rate']),
            'iterations': int(perturb(current_params['iterations']))
        }

        # Upewnij się, że parametry są w sensownym zakresie
        new_params['cooling_rate'] = max(0.8, min(0.9999, new_params['cooling_rate']))
        new_params['iterations'] = max(100, new_params['iterations'])

        new_solution, new_distance = simulated_annealing(
            distance_matrix = distance_matrix,
            initial_temperature = new_params['initial_temp'],
            cooling_rate = new_params['cooling_rate'],
            max_iterations = new_params['iterations']
        )

        cost_history.append(new_distance)

        delta = new_distance - current_distance

        if delta < 0 or random.random() < math.exp(-delta / param_temp):
            # Akceptuj lepsze lub gorsze rozwiązanie z pewnym prawdopodobieństwem
            current_params = new_params
            current_distance = new_distance

            if new_distance < best_distance:
                best_distance = new_distance
                best_params = new_params

        param_temp *= 0.995
        print(_)

    plt.figure(figsize=(10, 5))
    plt.plot(cost_history, marker='o')
    plt.title("Postęp optymalizacji parametrów (symulowane wyżarzanie parametrów)")
    plt.xlabel("Iteracja")
    plt.ylabel("Najlepszy koszt (długość ścieżki)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return best_params, best_distance
