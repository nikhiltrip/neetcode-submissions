class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []
        for word in strs:
            pieces.append(str(len(word)))
            pieces.append("#")
            pieces.append(word)

        return "".join(pieces)

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            digit = ""
            while s[i] != "#":
                digit += s[i]
                i += 1
            i += 1
            length = int(digit)
            if length == 0:
                result.append("")
                continue
            start = i
            result.append(s[start:length+start])
            i = length + start

        return result
