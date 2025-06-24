# implementation of dynamic array in python
# geeksforgeeks
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError("item is out of bound")
        return  self.A[item]

    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1


    # delete item from the end of array
    def __delete__(self):
        if self.n == 0:
            print("Array is empty deletion not Possible")
            return
        self.A[self.n-1] = 0
        self.n -= 1


    # delete items from the specified index
    def removeAt(self, index):
        if self.n == 0:
            print("Array is empty detection not Possible")
            return
        if index < 0 or index >= self.n:
            return IndexError("Index out of bound... deletion not possible")
        if index == self.n-1:
            self.A[index] = 0
            self.n -= 1
            return
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        self.A[self.n-1] = 0
        self.n -= 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print(len(arr))
print(arr[1])
print(arr[2])

arr.removeAt(1)
print(len(arr))
arr.append(5)
print(len(arr))
for i in arr:
    if i < 0:
        break
    print(i)
