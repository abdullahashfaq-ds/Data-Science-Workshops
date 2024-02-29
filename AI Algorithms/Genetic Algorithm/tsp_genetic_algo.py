"""TRAVELING SALESMAN PROBLEM | GENETIC ALGORITHM"""

from random import sample, choices, random

# Global Variables
POPULATION_SIZE = 10
GENERATIONS = 1000


def create_population(cities: int) -> list:
    """Create an Initial Population"""
    return [
        sample(
            range(cities), cities
        )
        for _ in range(POPULATION_SIZE)
    ]


def calculate_distance(route: list, distance_matrix: list) -> int:
    """Fitness Evaluation"""
    total = 0
    for i in range(len(route)-1):
        total += distance_matrix[route[i]][route[i+1]]
    total += distance_matrix[route[-1]][route[0]]
    return total


def order_crossover(p1: list, p2: list) -> list:
    """Function to perform Order Crossover (OX)"""
    start, end = sorted(
        sample(
            range(len(p1)), 2
        )
    )
    child = p1[start: end+1]
    remaining = [
        gene for gene in p2 if gene not in child
    ]
    child += remaining
    return child


def mutate(route: list) -> list:
    """Function to perform Mutation (swapping)"""
    idx1, idx2 = sorted(
        sample(
            range(len(route)), 2
        )
    )
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


def genetic_algorithm(distance_matrix: list) -> tuple:
    cities = len(distance_matrix)

    # Step 01. Initialization
    population = create_population(cities)

    for _ in range(GENERATIONS):
        # Step 02. Fitness Evaluation
        # Higher fitness corresponds to shorter distances.
        fitness = [
            1 / calculate_distance(
                route, distance_matrix
            )
            for route in population
        ]

        # Step 03. Selection
        indices = choices(
            range(POPULATION_SIZE), weights=fitness, k=2
        )
        parent1 = population[indices[0]]
        parent2 = population[indices[1]]

        # Step 04. Crossover
        offspring = order_crossover(parent1, parent2)

        # Step 05. Mutation
        if random() < 0.10:
            offspring = mutate(offspring)

        # Step 06. Replacement
        min_fitness_index = min(
            range(POPULATION_SIZE),
            key=lambda x: fitness[x]
        )
        population[min_fitness_index] = offspring

    # Solution Extraction
    best_route_index = max(
        range(POPULATION_SIZE),
        key=lambda x: fitness[x]
    )
    best_route = population[best_route_index]
    best_distance = calculate_distance(best_route, distance_matrix)

    return best_route, best_distance


if __name__ == "__main__":
    distance_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    best_route, best_distance = genetic_algorithm(distance_matrix)

    print("Best Route:", end=" ")
    for city in best_route:
        print(f"{city} -> ", end="")
    print(best_route[0])

    print(f"Best Distance: {best_distance}")
