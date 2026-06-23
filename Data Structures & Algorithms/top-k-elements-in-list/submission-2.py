class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        c=[]
        b = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
        x=list(b.keys())
        i=0
        while(k>0):
            c.append(x[i])
            i+=1
            k-=1
        return c