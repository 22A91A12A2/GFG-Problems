class Solution:
    def substrCount(self, s, k):
        # code here
        cnt=0
        for i in range(len(s)-k+1):
            sub=s[i:i+k]
            if len(set(sub))==k-1:
                cnt+=1
        return cnt    