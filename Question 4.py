import itertools

# List
my_list = ['A', 'B', 'C', 'D', 'E']

# All combinations of all lengths
print("Combinations:")
for r in range(1, len(my_list) + 1):
    combinations = itertools.combinations(my_list, r)
    for combo in combinations:
        print(combo)

# All permutations of all lengths
print("\nPermutations:")
for r in range(1, len(my_list) + 1):
    permutations = itertools.permutations(my_list, r)
    for perm in permutations:
        print(perm)

