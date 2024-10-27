print("Enter the numbers of element: ")
n = int(input()) #input number of buttons
print("Enter the elements: ")
arr = list(map(int, input().split())) #input array 1 and 0 (1:fastened, 0: not fastened)
print("Enter the Sum: ")
s = int(input())
def find_subArr(arr, n, s):
    startIndex = 0
    currentSum = 0
    for end in range(n):
        currentSum += arr[end]
        while currentSum > s and startIndex < end:
            currentSum -= arr[startIndex]
            startIndex += 1;

        if currentSum == s:
            return [startIndex + 1, end + 1]
    return [-1]
print(find_subArr(arr, n, s))