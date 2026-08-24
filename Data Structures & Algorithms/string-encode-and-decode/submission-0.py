class Solution:
    """
    ["devvvvvvvvvvv", "desai"]
    13*devvvvvvvvvvv4*desai
    i
     j
    
    length = int(s[i:j+1])
    res.append(s[j+1:j+length+1])
    i += length + 2
    j += length + 1
    """
    def encode(self, ipt: List[str]) -> str:
        # <lenght># will be used in start of each word
        out = ""
        for i in ipt:
            out += str(len(i)) + '*' + str(i)
        return out

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '*':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res