class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:        
        l=[]
        j=True
        n=0
        while  n!=len(arr2) and arr2[n] in arr1 :
               l.append(arr2[n])
               arr1.remove(arr2[n])
               if arr2[n] not in arr1:
                  n+=1
        return l+sorted(arr1)        

                      
