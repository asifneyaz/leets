class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        s2 = s1[-1]
        return len(s2)