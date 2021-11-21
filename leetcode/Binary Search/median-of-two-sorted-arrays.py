def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: merge arrays
        merge_arr = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge_arr.append(nums1[i])
                i += 1
            else:
                merge_arr.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            merge_arr.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            merge_arr.append(nums2[j])
            j += 1
        
        # Step 2: find median using floor division
        arr_len = len(merge_arr)
        mid = arr_len // 2
        
        if (arr_len % 2) == 0: # Checking if length of merged array is even
            median = float((merge_arr[mid-1] + merge_arr[mid]) / 2) # Keeping in mind index starts at zero
        else:
            median = float(merge_arr[mid])
            
        return median