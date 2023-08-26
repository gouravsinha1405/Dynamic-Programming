class Solution:
    #----Tabulation(bottom up)---#
    def tabulation(self, nums, target, N):
        for sum_ in range(target+1):
            for num in range(N+1):
                if sum_ == 0:
                    self.dp[sum_][num] = True
                if num == 0 and sum_ != 0:
                    self.dp[sum_][num] = False
                if num >= 1 and sum_ >= 1:
                    if nums[num-1] <= sum_:
                        self.dp[sum_][num] = self.dp[sum_-nums[num-1]][num-1] or self.dp[sum_][num-1]
                    else:
                        self.dp[sum_][num] = self.dp[sum_][num-1]
        return self.dp[target][N]

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        N = len(nums)
        self.dp = [[-1 for _ in range(N+1)] for _ in range(target+1)]
        return self.tabulation(nums,target,N)

