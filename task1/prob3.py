def intersection(nums1, nums2):
    # Convert the arrays to sets
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Find the intersection of the two sets
    result = set1 & set2
    
    # Return the intersection as a list
    return list(result)
