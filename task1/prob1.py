def find_length_of_lcis(nums):
    # If the array is empty, return 0
    if not nums:
        return 0

    # Initialize variables to track the max and current length
    max_length = 1
    current_length = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # Check if the sequence is increasing
            current_length += 1  # Extend the current sequence
            max_length = max(max_length, current_length)  # Update max_length if needed
        else:
            current_length = 1  # Reset the current sequence length

    return max_length

# Example usage
nums1 = [1, 3, 5, 4, 7]
nums2 = [2, 2, 2, 2, 2]

# Outputs
print(find_length_of_lcis(nums1))  # Output: 3
print(find_length_of_lcis(nums2))  # Output: 1
