class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''.join (ch.lower() for ch in s if ch.isalnum()) #"Was it a car or a cat I saw?"-> ?(alnum)
        #return clean[::-1] == clean #slice opr
        temp = ''.join(reversed(clean)) #reversed->return lazy iterator object-->so join
        return temp == clean
