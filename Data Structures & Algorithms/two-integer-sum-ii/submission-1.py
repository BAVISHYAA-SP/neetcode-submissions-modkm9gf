class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            b=target-numbers[i]
            if(b in numbers and numbers.index(b)!=i):
                a=[i+1,numbers.index(b)+1]
        return sorted(a)


        