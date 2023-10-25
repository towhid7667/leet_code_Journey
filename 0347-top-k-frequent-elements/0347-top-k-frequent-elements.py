class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        f = [[] for i in range(len(nums) + 1)]
        for i in nums:
            c[i] = 1 + c.get(i , 0)
        for v, j in c.items():
            f[j].append(v)

        r = []
        for i in range(len(f) -1, 0, -1):
            for n in f[i]:
                r.append(n)
                if len(r) == k:
                    return r       