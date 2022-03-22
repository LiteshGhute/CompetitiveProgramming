#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        lst = []
        
        for i in range(n):
            lst.append([start[i],end[i]])
            
        lst = [num for num in sorted(lst, key=lambda x: x[1])]
        
        count = 0
        prev = -1
        
        for ls in lst:
            if ls[0] > prev:
                count += 1
                prev = ls[1]
                
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
