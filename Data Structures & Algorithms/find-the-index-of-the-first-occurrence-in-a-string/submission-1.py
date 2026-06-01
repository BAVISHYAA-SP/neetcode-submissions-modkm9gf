class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=0
        b=0
        i=0
        m=len(haystack)
        n=len(needle)
        while(a<m and b<n):
            if(haystack[a]==needle[b]):
                a=a+1
                b=b+1

            else:
                i=i+1
                b=0
                a=i
           
            if(b==n):
                return i
        else:
            return -1
