class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        liste=[[] for i in range(len(nums)+1)]
        for k in nums:
            hashmap[k]=hashmap.get(k,0)+1
        for key,value in hashmap.items():
            liste[value].append(key)
        sls=[]    
        for i in range(len(liste)-1,0,-1):
            for j in liste[i]:
                sls.append(j)
                if len(sls)== k:
                    return sls


           
        