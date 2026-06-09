class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        for i in digits:
            a+=str(i)
        b=str(int(a)+1)
        res=[]
        for i in b:
            res.append(i)
        return res

        