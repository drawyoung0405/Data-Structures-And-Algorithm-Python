from random import shuffle
 # My solution:
# Step 1: Find max of array
# Step 2: Create the continuous array from min to max
# Step 3: XOR both arrays to find the missing number
print("Enter the elements of array: ")
arr = list(map(int, input().split())) #The elements in the array are separated by a single space.
def create_continous_array(arr):
    if not arr:
        return[]
    min_value = min(arr)
    max_value = max(arr)
    return list(range(min_value, max_value + 1))
#create continuos array from min to max
new_array = list(create_continous_array(arr))
missing_number = 0
for i in new_array+arr: # XOR with both original and continuous array
    missing_number ^= i

print(missing_number)