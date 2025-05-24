def contains_nearby_duplicate(nums, k):
    index_map = {}

    for i, num in enumerate(nums):
        print(f"Index {i}, Value {num}")
        if num in index_map:
            diff = i - index_map[num]
            print(f"Seen before at index {index_map[num]}, difference = {diff}")
            if diff <= k:
                print("→ Duplicate found within range!")
                return True
        index_map[num] = i
        print(f"Stored index of {num} as {i}")

    print("No nearby duplicates found.")
    return False

# Example tests
print("\nTest 3:")
print("Result:", contains_nearby_duplicate([1, 2, 3, 1], 3))  # True

print("\nTest 4:")
print("Result:", contains_nearby_duplicate([1, 0, 1, 1], 1))  # True

print("\nTest 5:")
print("Result:", contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))  # False
