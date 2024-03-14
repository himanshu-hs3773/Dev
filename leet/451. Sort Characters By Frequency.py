class Solution:
    def frequencySort(self, s: str) -> str:
        freq: dict = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        return "".join([k * v for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)])
