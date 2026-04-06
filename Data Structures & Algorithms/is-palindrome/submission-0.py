class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a="".join(i for i in s if i.isalnum())
        b=a[::-1]
        if a==b:
            return True
        else:
            return False