class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=list(set(nums))
        a.sort()
        print(a)
        res=1
        cnt=1
        for i in range(1,len(a)):
            if(a[i]-a[i-1]==1):
                print("cnt",cnt)
                cnt+=1
                if(cnt>res):
                    res=cnt
            else:
                if(cnt>=res):
                    res=cnt
                    cnt=1
        if(len(nums)!=0):
            return res
        else:
            return 0

