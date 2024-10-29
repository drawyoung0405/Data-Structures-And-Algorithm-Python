# Data-Structures-And-Algorithm-Python  
#### This project was referenced from websites: codeforce, leetcode,...
Let's learn DSA!
# Dynamic Array & String
# 1. Fashion In Berland 
According to rules of the Berland fashion, a jacket should be fastened by all the buttons except only one, but not necessarily it should be the last one. Also if the jacket has only one button, it should be fastened, so the jacket will not swinging open.
You are given a jacket with N buttons. 

Determine if it is fastened in a right way.

# Input Format

 The first line contains integer N(1 ≤ N ≤ 1000) - The number of buttons on the jacket.

 The second line contains N integers a<sub>i</sub> (0 &le; a<sub>i</sub> &le; 1). The number a<sub>i</sub> = 0 if the i-th button is not fastened. Otherwise a<sub>i</sub> = 1.  

# Output Format
In the only line print the word YES if the jacket is fastened in a right way. Otherwise print the word NO.
# Sample test

| Input       | Output |
|-------------|--------|
| 3<br/>1 0 0 | NO     |
| 3<br/>1 0 1 | YES    |

# 2. Indexes of Subarray Sum
Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

# Input Format

 The first line contains integer N(1 ≤ N ≤ 1000) - The number of array elements. 

 The second line contains N integers a<sub>i</sub> (0 &le; a<sub>i</sub> &le; 1)  

 The third line integer S (sum of sub array desired by user) 

# Output Format
In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
# Sample test

| Input                  | Output |
|------------------------|--------|
| 5<br/>1,2,3,7,5<br/>12 | 2 4    |
| 3<br/>7,2,1<br/>2      | 2 2    |

# 3. Finding the missing number of an array (Easy)
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
### Example 1:

**Input**: nums = [3,0,1]</br>
**Output**: 2</br>
**Explanation**: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

### Example 2:</br>
**Input**: nums = [0,1]</br>
**Output**: 2</br>
**Explanation**: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

### Example 3:

**Input**: nums = [9,6,4,2,3,5,7,0,1] </br>
**Output**: 8

**Explanation**: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 **Constraints**:

- n == nums.length</br>
- 1 <= n <= 104</br>
- 0 <= nums[i] <= n </br>
- All the numbers of nums are unique.
 
# 4. Three Sum 
Given an array of integers nums and an integer target, return indices of the three numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

**Example**


| Input                   | Output |
|-------------------------|--------|
| 1, 2, 3, 7, 5, 8<br/>10 | 1 2 4  |
| 7, 2, 1, 9, 5<br/>8     | 1 2 4  |




 

