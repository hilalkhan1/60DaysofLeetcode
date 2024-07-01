#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def passedBy(self, a, b):
        # Code here
        return a+1, b+2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        a, b = list(map(int, input().split()))
        ob = Solution()
        res = ob.passedBy(a, b)
        print(res[0], res[1])
# } Driver Code Ends