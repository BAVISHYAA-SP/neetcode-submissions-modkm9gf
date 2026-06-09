class Solution:
    def isHappy(self, n: int) -> bool:
        x=str(n)
        a=[]
        a.append(n)
        while(True):
            cnt=0
            for i in x:
                cnt+=(int(i)**2)
            if(cnt==1):
                return True
            else:
                if(cnt not in a):
                    a.append(cnt)
                    x=str(cnt)
                else:
                    return False
