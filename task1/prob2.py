def merge(nums1, m, nums2, n):
    # Start merging from the end of nums1
    i = m - 1  # Last valid element in nums1
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last position in nums1

    # Merge nums1 and nums2 from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:  # If nums1 element is larger
            nums1[k] = nums1[i]
            i -= 1
        else:  # If nums2 element is larger or equal
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Add remaining elements from nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example Usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
