def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            mid = (first + last) // 2
            
            if nums[mid] == target:
                return mid
            # left sorted portion
            if nums[first] <= nums[mid]:
                if target > nums[mid]:
                    first = mid + 1
                elif target < nums[first]:
                    first = mid + 1
                else:
                    last = mid - 1
            # right sorted portion
            else:
                if target < nums[mid]:
                    last = mid - 1
                elif target > nums[last]:
                    last = mid - 1
                else:
                    first = mid + 1
                    
        return -1