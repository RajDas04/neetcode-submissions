# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        if(len(pairs) <= 0):
            return result
        result.append(pairs[:])
        for i in range(1, len(pairs)):
            while(i > 0 and pairs[i].key < pairs[i-1].key):
                temp = pairs[i-1]
                pairs[i-1] = pairs[i]
                pairs[i] = temp
                i -= 1
            result.append(pairs[:])
        return result