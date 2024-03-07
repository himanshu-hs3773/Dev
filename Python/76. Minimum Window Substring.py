import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """265/267"""
        # t_map = {}
        # res = ""
        #
        # for c in t:
        #     t_map[c] = 1 + t_map.get(c, 0)
        #
        # i = 0
        # while i < len(s):
        #     tmp_map = copy.deepcopy(t_map)
        #     if s[i] not in tmp_map:
        #         i += 1
        #         continue
        #     j = 0
        #     while i + j < len(s):
        #         if s[i + j] in tmp_map:
        #             tmp_map[s[i + j]] -= 1
        #             if tmp_map[s[i + j]] == 0:
        #                 del tmp_map[s[i + j]]
        #             if not tmp_map:
        #                 tmp = s[i: i + j + 1]
        #                 if not res:
        #                     res = tmp
        #                 else:
        #                     res = res if len(res) <= len(tmp) else tmp
        #                 break
        #         j += 1
        #     i += 1
        # return res

        if t == "":
            return ""
        t_map, window = {}, {}
        for c in t:
            t_map[c] = t_map.get(c, 0)

        have, need = 0, len(t_map)

        res, res_len = [-1, -1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_map and window[c] == t_map[c]:
                have += 1

            while have == need:
                if (r - 1 + l) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if res_len != float("infinity") else ""



