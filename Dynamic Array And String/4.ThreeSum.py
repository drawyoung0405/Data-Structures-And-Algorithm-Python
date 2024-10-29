from typing import  List
print("target: ")
target = int(input())
print("enter elements: ")
nums = list(map(int, input().split()))
def threeSum( nums, target) -> List[int]:
        n = len(nums)
        for i in range(n-2):
            left, right = i+ 1, n -1
            while left<right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return [i, left, right]
                elif current_sum < target:
                    left += 1
                else:
                    right -=1
        return []
print(threeSum(nums, target))