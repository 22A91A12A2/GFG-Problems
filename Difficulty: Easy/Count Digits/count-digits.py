#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        l=[]
        cnt=0
        a=n
        while(n>0):
            v=n%10
            if(v!=0 and a%v==0):
                cnt=cnt+1
            n=n//10
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends