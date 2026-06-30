class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for k in strs:
            key=''.join(sorted(k))
            if key not in dic:
                dic[key]=[]
            dic[key].append(k)    
        l=[values for key,values in dic.items()]
        return l
        




        