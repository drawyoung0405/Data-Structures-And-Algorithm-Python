from typing import List

print("Enter target")
target = int(input())
print("Enter Array")
raw_input = input()
if ' ' in raw_input:
    # Xử lý chuỗi số có dấu cách, ví dụ: "1 2 3"
    nums = list(map(int, raw_input.split()))
else:
    # Xử lý chuỗi số không có dấu cách, ví dụ: "123"
    nums = [int(char) for char in raw_input]

def twoSum(nums: List[int], target) -> List[int]:
    num_store = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_store:
            return [num_store[complement], i]
        num_store[num] = i
    return []


print(twoSum(nums, target))
