class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        '''
        One liner
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        '''
        dict_s = {}
        dict_t = {}

        if len(s) != len(t):
            return False

        if s == t:
            return True

        for i in range(len(s)):
            if s[i] not in dict_s and t[i] not in dict_t:
                dict_s[s[i]] = t[i]
                dict_t[t[i]] = s[i]
            elif s[i] in dict_s and t[i] not in dict_t:
                return False
            elif s[i] not in dict_s and t[i] in dict_t:
                return False
            else:
                if dict_s[s[i]] != t[i] or dict_t[t[i]] != s[i]:
                    return False
        return True
