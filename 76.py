class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        counter, window = {}, {}
        for c in t:
            counter[c] = 1 + counter.get(c, 0)
        l = 0
        have, need = 0, len(counter)
        result, result_length = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in counter and window[c] == counter[c]:
                have += 1
            while have == need:
                if (r - l + 1) < result_length:
                    result = [l, r]
                    result_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        if result_length != float("infinity"):
            return s[l:r + 1]
        else:
            return ""
