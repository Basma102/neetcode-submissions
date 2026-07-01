class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        liste=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for key,value in hashmap.items():
            if value>=k:
                liste.append(key)
   
        return liste   
        