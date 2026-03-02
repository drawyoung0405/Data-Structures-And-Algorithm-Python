from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a list that add up to a target value.

    This function uses a dictionary (hash map) to store numbers that have been seen
    and their indices. This allows for a single pass through the list, resulting
    in an efficient O(n) time complexity.

    :param nums: A list of integers.
    :param target: The integer sum to find.
    :return: A list containing the indices of the two numbers, or an empty list if no solution is found.
    """
    # Create a dictionary to store numbers we've seen and their indices.
    num_store = {}
    # Iterate through the list with both index (i) and value (num).
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target.
        complement = target - num
        # Check if the complement exists in our dictionary.
        if complement in num_store:
            # If it exists, we found a solution.
            return [num_store[complement], i]
        # If the complement is not found, add the current number and its index to the dictionary
        # for future lookups.
        num_store[num] = i
    # If the loop completes without finding a solution, return an empty list.
    return []

# This block ensures the following code only runs when the script is executed directly.
if __name__ == "__main__":
    target = int(input("Enter target: "))
    # Get the array of numbers from the user, assuming they are space-separated.
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

    # Call the function and print the result.
    result = twoSum(nums, target)
    print(f"Result: {result}")
