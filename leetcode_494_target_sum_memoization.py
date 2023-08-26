class Solution:
    def memoize(self, nums, N, total_sum):
        if (N, total_sum) in self.dp:
            return self.dp[(N,total_sum)]
        if total_sum == self.target and N == 0:
           return 1
        if N == 0:
            return 0
        positive = self.memoize(nums, N-1, total_sum)
        negative = self.memoize(nums, N-1, total_sum + 2*(-nums[N-1]))
        self.dp[(N,total_sum)] = positive + negative
        return self.dp[(N,total_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        self.dp = {}
        self.diff = target
        total_sum = sum(nums)
        self.target = target
        return self.memoize(nums, N, total_sum)
