class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        p=0
        m=len(s)
        n=len(t)
        cnt=0
        while(p<n and l<m):
            if(s[l]==t[p]):
                l=l+1
                p=p+1
                cnt+=1
            else:
                p=p+1
        if(cnt==m):
            return True
        else:
            return False
