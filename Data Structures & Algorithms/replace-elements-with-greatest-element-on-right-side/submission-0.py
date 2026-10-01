class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = len(arr)
        ans = [0] * a
        for i in range(a):
            right = -1
            for j in range(i+1, a):
                right = max(right, arr[j])
            ans[i] = right
        return ans