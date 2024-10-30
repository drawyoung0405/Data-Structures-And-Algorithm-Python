from typing import List

print("Enter target")
target = int(input())
print("Enter Array")
nums = list(map(int, input().split()))


def twoSum(nums: List[int], target) -> List[int]:
    num_store = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_store:
            return [num_store[complement], i]
        num_store[num] = i
    return []


print(twoSum(nums, target))
