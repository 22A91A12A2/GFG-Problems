
class Solution:
    def isBalanced(self, s):
        # code here
        n = len(s)
        l = []
        for i in range(n):
            c = s[i]
            if c== '(' or c== '{' or c== '[':
                l.append(c)
            else:
                if not l:
                    return False
                else:

                    top = l[-1]

                    l.pop()

                    if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):

                        return False

        return True if len(l) == 0 else False




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

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
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends