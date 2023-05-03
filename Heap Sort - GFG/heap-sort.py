#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.

            
    def heapify(self,arr, n, i):
        left = 2*i + 1
        right = 2*i + 2
        largest_child = i
        if left < n and arr[left] > arr[largest_child]:
            largest_child = left
        if right < n and arr[right] > arr[largest_child]:
            largest_child = right
        
        if i != largest_child:
            arr[i] , arr[largest_child] = arr[largest_child] , arr[i]
            i = largest_child
            self.heapify(arr,n, i) 
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        #build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr ,len(arr), i)
        
        # code here
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(len(arr)):
            arr[len(arr) - i - 1] , arr[0] = arr[0] , arr[len(arr) - i - 1]
            
            self.heapify(arr, len(arr) - i - 1, 0)
            
            
        return  arr
        
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends