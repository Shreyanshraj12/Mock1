def moveZeroes(nums):
    i = 0  
    j = 0  
    while i < len(nums):
        if nums[i] != 0:
            
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1

    while j < len(nums):
        nums[j] = 0
        j += 1

    return nums
nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))  

nums2 = [0]
print(moveZeroes(nums2))  
