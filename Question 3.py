# Function to generate combinations
def generate_combinations(current, index, lst):
    if index == len(lst):
        if current:
            print(tuple(current))
        return
    generate_combinations(current, index + 1, lst)
    generate_combinations(current + [lst[index]], index + 1, lst)
    
# Function to generate permutations
def generate_permutations(lst, start, end):
    if start == end:
        print(tuple(lst))
    else:
        for i in range(start, end):
            lst[start], lst[i] = lst[i], lst[start]  # Swap
            generate_permutations(lst, start + 1, end)
            lst[start], lst[i] = lst[i], lst[start]  # Swap back to backtrack
# List
my_list = ['A', 'B', 'C', 'D', 'E']
# All combinations
print("Combinations:")
generate_combinations([], 0, my_list)
# All permutations
print("\nPermutations:")
generate_permutations(my_list, 0, len(my_list))

