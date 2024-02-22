from itertools import permutations

# Given cities and distances
cities = ["Charlotte", "Memphis", "Orlando", "Atlanta"]
distances = {
    "Charlotte": {"Charlotte": 0, "Memphis": 100, "Orlando": 120, "Atlanta": 40},
    "Memphis": {"Charlotte": 100, "Memphis": 0, "Orlando": 80, "Atlanta": 50},
    "Orlando": {"Charlotte": 120, "Memphis": 80, "Orlando": 0, "Atlanta": 90},
    "Atlanta": {"Charlotte": 40, "Memphis": 50, "Orlando": 90, "Atlanta": 0}
}

# Function to calculate total distance of a tour
def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour)):
        if i == len(tour) - 1: # if last city, return to first
            total_distance += distances[tour[i]][tour[0]]
        else:
            total_distance += distances[tour[i]][tour[i + 1]]
    return total_distance

# Generate all possible tours
all_possible_tours = permutations(cities)

# Initialize variables for the shortest tour and distance
shortest_tour = None
shortest_distance = float('inf')  # Set to positive infinity initially

# Iterate through all possible tours
for tour in all_possible_tours:
    # Calculate the distance of the current tour
    current_distance = calculate_distance(tour)

    # Check if the current tour has a shorter distance than the current shortest
    if current_distance < shortest_distance:
        shortest_distance = current_distance
        shortest_tour = tour

# Print the results
print(f"Shortest tour: {shortest_tour} then back to Charlotte with a distance of {shortest_distance}km.")

