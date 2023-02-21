#User function Template for python3

class Solution: 
    def select(self, arr, i):
        min_index=i
        # code here 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        return min_index
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min_index=i
            min_index=self.select(arr,i)
            if min_index!=i:
                arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends