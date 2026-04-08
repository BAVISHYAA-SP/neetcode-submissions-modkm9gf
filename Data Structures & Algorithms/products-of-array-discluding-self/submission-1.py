class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        c=0
        for i in nums:
            if (i==0):
                c+=1
            else:
                a=a*i
        b=[]
        if (c==1):
            for i in nums:
                if(i==0):
                    b.append(a)
                else:
                    b.append(0)
        elif(c>1):
            for i in nums:
                b.append(0)
        else:
            for i in nums:
                b.append(a//i)

        return b





        

        