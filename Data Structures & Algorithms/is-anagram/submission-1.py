class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in t:
            cnt[ord(c)- ord('a')] -= 1
        return all(c == 0 for c in cnt)