class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): #it lets you skip in o(1),saving time
            return False;
        return sorted(s) == sorted(t);

#return Counter(s) == Counter(t) same -->uses dict mapping