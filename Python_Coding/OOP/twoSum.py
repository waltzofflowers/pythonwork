import random

class Solution(object):
    def twoSum(self, nums, target):
        indices = []

        while True:
            a_index = random.randint(0, len(nums) - 1)
            b_index = random.randint(0, len(nums)- 1)
            a = nums[a_index]
            b = nums[b_index]

            if a_index != b_index:
                if a + b == target:
                    indices.append(a_index)
                    indices.append(b_index)
                    return indices
        return []

nums = [2, 7, 11, 15]

target = 9

sol = Solution()
print(sol.twoSum(nums, target))