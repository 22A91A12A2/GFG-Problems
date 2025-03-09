#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        
        #arr : given array
        #n : size of the array
        c={}
        for i in arr:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
        for i in range(len(arr)):
            if c[arr[i]]>1:
                return i+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))
        print("~")

# } Driver Code Ends