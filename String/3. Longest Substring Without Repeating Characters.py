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
                            l.append(len(s)-1)
                            return max(l)
                        else:
                            l.append(len(s[j:i-1]))
                            return max(l)
                l.append(len(s[j:i-1]))
                j = s[:i].index(str(s[i]),j+1,i)
                i = i + 1
            return max(l)
        elif len(s) == 1:
            return 1
        else:
            return 0