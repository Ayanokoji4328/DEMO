def sum_of_subsets(arr, target, subset=[], index=0, current_sum=0):
    if current_sum == target:
        print(subset)
        return
    if index >= len(arr) or current_sum > target:
        return
    # Include the current element and recurse
    sum_of_subsets(arr, target, subset + [arr[index]], index + 1, current_sum + arr[index])
    # Exclude the current element and recurse
    sum_of_subsets(arr, target, subset, index + 1, current_sum)

# Example usage
arr = [10, 7, 5, 18, 12, 20, 15]
target_sum = 35
print("Subsets with sum", target_sum, "are:")
sum_of_subsets(arr, target_sum)