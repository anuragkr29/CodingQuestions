#Please visit https://www.cs.cmu.edu/~avrim/451f12/lectures/lect0906.pdf for detailed explanation
from math import floor
#function returning the medians for a given array
def get_medians(arr):
    temp = []
    l = len(arr)
    if l==1:
        return arr
    if l>5:
        for i in range(0,l-5,5):
            temp.append(sorted(arr[i:i+5])[2])
        if i<l:
            temp.append(sorted(arr[i+5:])[floor(len(arr[i+5:])/2)])
    else:
        temp.append(sorted(arr)[floor(len(arr)/2)])
    return temp
#function to find the 'k'th smallest number in the array 'arr' 
#Computational Complexity -- O(n)
def kthSmallest(arr , k):
    if len(arr) <= 10:
        arr.sort()
        return arr[k-1]
    medians = get_medians(arr);
    length = len(arr)
    if k > 0 and k <length :
        medOfMedians = kthSmallest(medians,floor(len(medians)/2))
        pivot = partition(arr , medOfMedians)
        if pivot == k-1 :
            return medOfMedians
        elif pivot > k-1:
            return kthSmallest(arr[0:pivot],k)
        elif pivot < k-1:
            return kthSmallest(arr[pivot+1:],k-pivot-1)
#function to partition a given array 'arr' using a pivot 'num'            
def partition(arr , num):
    r = len(arr)-1
    n = arr.index(num)
    arr[n] , arr[r] = arr[r] , arr[n]
    last = -1
    for j in range(0 , r):
        if arr[j] <= num:
            last = last + 1
            if last < j :
                arr[last] , arr[j] = arr[j] , arr[last]
    if last + 1 < r :
        arr[last+1] , arr[r] = arr[r] , arr[last+1]
    return last+1
