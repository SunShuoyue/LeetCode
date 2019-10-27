class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        i = 0
        for j in range(1, len(s)):
            if s[j] in s[i:j] or len(set(s[i:j])) != (j - i):
                i += 1
        return j - i + 1


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) > 1:
            l = []
            i = 1
            while i < len(s) and s[i] not in s[:i]:
                i += 1
                if i == len(s):
                    return len(s)
            l.append(len(s[:i]))
            j = s[:i].index(str(s[i]))
            i = i + 1
            while i < len(s):
                while s[i] not in s[j:i]:
                    i += 1
                    if i == len(s):
                        if j == 0:
                            l.append(len(s) - 1)
                            return max(l)
                        else:
                            l.append(len(s[j:i - 1]))
                            return max(l)
                l.append(len(s[j:i - 1]))
                j = s[:i].index(str(s[i]), j + 1, i)
                i = i + 1
            return max(l)
        elif len(s) == 1:
            return 1
        else:
            return 0
