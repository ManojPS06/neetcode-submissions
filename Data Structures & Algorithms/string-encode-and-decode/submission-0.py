class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        mainloop = 0
        while mainloop < len(s):
            numsepr = mainloop
            while s[numsepr] != "#":
                numsepr += 1
            length = int(s[mainloop:numsepr])
            """           0123456  
                          10#abcd....->int(0,1)->length=10  
            """            
            start = numsepr + 1
            result.append(s[start:start + length])
            """
                        start->delimiter_idx(#)+1->string starts->length  || slice[start:stop]
            """
            mainloop = start + length
        return result