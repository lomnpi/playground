nums1 = [1, 2, 5]
nums2 = [3, 4, 5, 6]

def merge_sorted_arrays(nums1, nums2):
    merged_arr = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_arr.append(nums1[i])
            i += 1
        else:
            merged_arr.append(nums2[j])
            j += 1
        
    while i < len(nums1):
        merged_arr.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged_arr.append(nums2[j])
        j += 1

    return merged_arr


print(merge_sorted_arrays(nums1, nums2))

