#Guide
# Step 1: Read the number of buttons N.
# Step 2: Read the button states, where each button is represented by 1 (fastened) or 0 (unfastened).
# Step 3: Based on the value of N:
# If N = 1, check if the only button is fastened (its value is 1). If it is, print YES; otherwise, print NO.
# If N > 1, count the number of unfastened buttons (0). If there is exactly one unfastened button, print YES. Otherwise, print NO.
#SOLUTION 1:
n = int(input()) #input number of buttons
arr = list(map(int, input().split())) #input array 1 and 0 (1:fastened, 0: not fastened)
def jacket(n , arr):
    if (n == 1 and arr == 1) :
        return True
    else:
        return False
    count = 0
    for i in range(arr):
        if arr[i] == 0:
            count += 1;
    if count == 1:
        return True
    else:
        return False

if jacket(n,arr):
    print("YES")
else:
    print("NO")
#SOLUTION 2:
# n = int(input())
# btns = list(map(int, input().split()))
#
# if (n ==1):
#     if(btns[0] == 1):
#         print("YES")
#     else:
#         print("NO")
# else:
#     unfastened = btns.count(0)
#     if unfastened == 1:
#         print("YES")
#     else:
#         print("NO")