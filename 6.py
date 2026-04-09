import itertools 
  
def generate_sample_space(elements, r): 
    print(f"Elements: {elements}, Outcome length: {r}\n") 
     
    # Permutations (order matters) 
    permutations = list(itertools.permutations(elements, r)) 
    print("Permutations:", permutations) 
    print("Total permutations:", len(permutations), "\n") 
     
    # Combinations (order does not matter) 
    combinations = list(itertools.combinations(elements, r)) 
    print("Combinations:", combinations) 
    print("Total combinations:", len(combinations)) 
  
# Example 
generate_sample_space(['A', 'B', 'C', 'D'], 2)
