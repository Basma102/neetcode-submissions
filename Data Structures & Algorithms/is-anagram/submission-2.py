class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        m={}
        for i in s:
            d[i]=d.get(i,0)+1
        for j in t:
            m[j]=m.get(j,0)+1   
        if d==m:
            return True
        return False    