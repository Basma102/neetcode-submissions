class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        liste=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        sortedDict=dict(sorted(hashmap.items(),key=lambda x:x[1],reverse=True))    
        for key in sortedDict:
            if k!=0:
                liste.append(key)
                k-=1
        return liste

           
        