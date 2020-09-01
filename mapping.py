class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = 0
        result = []
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                result.append(alpha(s[i:i+2]))
                i += 3
            else:
                result.append(alpha(s[i]))
                i += 1
        return "".join(result)

val=Solution()
s=input()
print(val.freqAlphabets(s))
