class Solution:
    def minSum(self, arr):
        # code here
        res=''
        carry=0
        n=len(arr)
        arr=sorted(arr)[::-1]
        for i in range(0,n,2):
            sm=carry
            sm+=arr[i]+(arr[i+1] if i+1<n else 0) 
            carry=sm//10
            res+=str(sm%10)
        res+=str(carry)
        res=res.rstrip('0')
        return res[::-1]