#User function Template for python3


class Solution:
    def findFirst(self,arr,n,x):
        low,high=0,n-1
        firstOccur=-1
        
        while(low<=high):
            mid=(low+high)//2
            
            if(arr[mid]==x):
                firstOccur=mid
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        
        return firstOccur
    
    def findLast(self,arr,n,x):
        low,high=0,n-1
        lastOccur=-1
        
        while(low<=high):
            mid=(low+high)//2
            
            if(arr[mid]==x):
                lastOccur=mid
                low=mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        
        return lastOccur
        
    def find(self, arr, n, x):
        first=self.findFirst(arr,n,x)
        
        if(first==-1): return [-1,-1]
        
        last=self.findLast(arr,n,x)
        
        return [first,last]

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends