#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        s={}
        l=[]
        for i in arr:
            if i in s:
                l.append(i)
            else:
                s[i] = 1
        for j in range(1, n+1):
            if j not in s:
                l.append(j)
                break
        return l






#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends