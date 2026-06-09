class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        cnt=0

        while(l<r):
            if(leftmax<rightmax):
                l+=1
                leftmax=max(leftmax,height[l])
                cnt+=(leftmax-height[l])
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                cnt+=(rightmax-height[r])
        return cnt


        