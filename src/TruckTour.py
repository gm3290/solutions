
def truckTour(petrolpumps):
    # Write your code here
    remaining = 0
    chosen_index = 0
    for index in range(len(petrolpumps)):
        gas = petrolpumps[index][0]
        distance = petrolpumps[index][1]
        remaining += gas-distance
        if remaining < 0:
            chosen_index = index+1
            remaining = 0

    return chosen_index


t = [[1, 5], [10, 3], [3, 4]]

print(truckTour(t))
