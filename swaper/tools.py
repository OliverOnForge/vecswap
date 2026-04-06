import random

# --- GENERATORS ---

def generate_full_int(n: int, value: int):
    """Creates a vector of n dimensions filled with the integer 'value'."""
    return [int(value)] * n

def generate_random_int(n: int, v_min: int, v_max: int):
    """Generates a vector of n random integers between v_min and v_max (inclusive)."""
    return [random.randint(v_min, v_max) for _ in range(n)]

def generate_range_int(start: int, stop: int, step: int = 1):
    """
    Generates a vector of integers from 'start' up to 'stop' (exclusive) 
    with a given 'step' increment.
    """
    return list(range(start, stop, step))

# --- OPERATORS ---

def add_vectors(vector_a: list, vector_b: list):
    """
    Performs element-wise addition of two vectors of the same length.
    Returns a new vector where result[i] = a[i] + b[i].
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length for addition.")
    
    return [a + b for a, b in zip(vector_a, vector_b)]

def subtract_vectors(vector_a: list, vector_b: list):
    """
    Performs element-wise subtraction of two vectors of the same length.
    Returns a new vector where result[i] = a[i] - b[i].
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length for subtraction.")
    
    return [a - b for a, b in zip(vector_a, vector_b)]

def interleave_from(vector_a: list, vector_b: list, start_index: int):
    """
    Interleaves vector_b into vector_a starting from start_index.
    Alternates one element from vector_a and one from vector_b.
    """
    result = vector_a[:start_index]
    rest_a = vector_a[start_index:]
    
    # Interleave while both lists have elements
    i = 0
    while i < len(rest_a) or i < len(vector_b):
        if i < len(rest_a):
            result.append(rest_a[i])
        if i < len(vector_b):
            result.append(vector_b[i])
        i += 1
            
    return result

# --- COMPARATORS ---

def are_equal(vector_a: list, vector_b: list):
    return vector_a == vector_b

def symmetric_difference(vector_a: list, vector_b: list):
    return list(set(vector_a) ^ set(vector_b))

def intersection(vector_a: list, vector_b: list):
    return list(set(vector_a) & set(vector_b))

def matched_indices(vector_a: list, vector_b: list):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length to locate matches.")
    return [i for i, (a, b) in enumerate(zip(vector_a, vector_b)) if a == b]

def mismatched_indices(vector_a: list, vector_b: list):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length to locate mismatches.")
        
    return [i for i, (a, b) in enumerate(zip(vector_a, vector_b)) if a != b]

# --- TRANSFORMERS ---

def normalize(vector: list):
    """Scales all values in the vector to a range between 0.0 and 1.0."""
    v_min, v_max = min(vector), max(vector)
    if v_max == v_min: 
        return [0.0] * len(vector)
    return [(x - v_min) / (v_max - v_min) for x in vector]

def increase(vector: list, increment: int):
    """Adds a fixed value to every element in the vector. Returns a new list."""
    return [val + increment for val in vector]

def decrease(vector: list, decrement: int):
    """Subtracts a fixed value from every element in the vector. Returns a new list."""
    return [val - decrement for val in vector]

def reflect_vertical(vector: list, center: int = 0):
    """
    Reflects each value vertically using 'center' as the axis.
    Formula: new_value = 2 * center - current_value.
    """
    for i in range(len(vector)):
        vector[i] = (2 * center) - vector[i]
    return vector

def fill_range(vector: list, value: int, start: int, stop: int):
    """
    Overwrites elements in the vector with a fixed 'value' 
    from 'start' index to 'stop' index (exclusive).
    """
    # Ensure indices are within the actual vector bounds
    safe_start = max(0, start)
    safe_stop = min(len(vector), stop)
    
    for i in range(safe_start, safe_stop):
        vector[i] = value
        
    return vector

def fill_pattern(vector: list, value: int, n: int, m: int):
    """
    Overwrites the vector with a 'value' using a repeating pattern:
    Modifies 'n' consecutive elements, then skips 'm' elements.
    """
    i = 0
    vector_len = len(vector)
    
    while i < vector_len:
        # Fill 'n' elements
        for _ in range(n):
            if i < vector_len:
                vector[i] = value
                i += 1
        
        # Skip 'm' elements
        i += m
            
    return vector

# --- REORDERING & STRUCTURAL ---

def mirror(vector: list):
    """Reverses the order of the elements in the vector."""
    return vector[::-1]

def random_swap(vector: list, changes: int):
    """
    Randomly swaps elements within the vector 'changes' times.
    Only successful swaps (different indices) count towards the total.
    """
    range_max = len(vector) - 1
    applied = 0
    while applied < changes:
        s1 = random.randint(0, range_max)
        s2 = random.randint(0, range_max)
        if s1 != s2:
            vector[s1], vector[s2] = vector[s2], vector[s1]
            applied += 1
    return vector

def reflect_on_axis(vector: list, axis_index: int):
    """
    Swaps elements around a specific index (axis) acting as a pivot.
    """
    n = len(vector)
    dist_to_start = axis_index
    dist_to_end = (n - 1) - axis_index
    radius = min(dist_to_start, dist_to_end)
    
    for i in range(1, radius + 1):
        left = axis_index - i
        right = axis_index + i
        vector[left], vector[right] = vector[right], vector[left]
    return vector

# --- SLICING & CLEANING ---

def trim_start(vector: list, n: int):
    """Removes the first n elements from the vector."""
    return vector[n:] if n < len(vector) else []

def trim_end(vector: list, n: int):
    """Removes the last n elements from the vector."""
    if n >= len(vector): return []
    return vector[:-n] if n > 0 else vector

def crop(vector: list, start: int, end: int):
    """Removes 'start' elements from the beginning and 'end' elements from the end."""
    if (start + end) >= len(vector): return []
    return vector[start:-end] if end > 0 else vector[start:]

# --- LIMITERS ---

def limit_upper(vector: list, max_value: int):
    """
    Clamps all values in the vector to a maximum threshold.
    Any value greater than max_value will be set to max_value.
    """
    for i in range(len(vector)):
        if vector[i] > max_value:
            vector[i] = max_value
    return vector

def limit_lower(vector: list, min_value: int):
    """
    Clamps all values in the vector to a minimum threshold.
    Any value smaller than min_value will be set to min_value.
    """
    for i in range(len(vector)):
        if vector[i] < min_value:
            vector[i] = min_value
    return vector

def clamp(vector: list, min_val: int, max_val: int):
    """
    Constrains all values within the [min_val, max_val] range.
    """
    for i in range(len(vector)):
        if vector[i] < min_val:
            vector[i] = min_val
        elif vector[i] > max_val:
            vector[i] = max_val
    return vector

def limit_upper_by_offset(vector: list, center: int, offset: int):
    """
    Clamps values that exceed a maximum threshold defined as (center + offset).
    Useful for preventing values from drifting too far above a reference point.
    """
    upper_bound = center + offset
    for i in range(len(vector)):
        if vector[i] > upper_bound:
            vector[i] = upper_bound
    return vector

def limit_lower_by_offset(vector: list, center: int, offset: int):
    """
    Clamps values that fall below a minimum threshold defined as (center - offset).
    Useful for ensuring values stay within a certain distance below a reference point.
    """
    lower_bound = center - offset
    for i in range(len(vector)):
        if vector[i] < lower_bound:
            vector[i] = lower_bound
    return vector

def limit_by_range(vector: list, center: int, offset: int):
    """
    Limits vector values within a range defined by a center and an offset.
    Example: center=10, offset=2 -> range is [8, 12].
    """
    lower_bound = center - offset
    upper_bound = center + offset
    
    for i in range(len(vector)):
        if vector[i] < lower_bound:
            vector[i] = lower_bound
        elif vector[i] > upper_bound:
            vector[i] = upper_bound
            
    return vector

# --- TESTING ---
if __name__ == '__main__':
    print('\nRUNNING MODULE IN TEST MODE\n')
    
    test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original: {test_array}")
    
    mirrored = anagram_shuffle(test_array,1)
    print(f"Mirrored: {mirrored}")
