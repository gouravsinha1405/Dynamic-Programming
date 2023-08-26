def lcs_memoization(nums1, nums2, m, n, dp, str_):
    if m == 0 or n == 0:
        return ""
    if (m,n,str_) in dp:
        return dp[(m,n,str_)]
    if nums1[m-1] == nums2[n-1]:
        str_ = lcs_memoization(nums1, nums2, m-1, n-1, dp, str_)
        str_ += nums1[m-1]
    else:
        str1 = lcs_memoization(nums1, nums2, m-1, n, dp, str_)
        str2 = lcs_memoization(nums1, nums2, m, n-1, dp, str_)
        if len(str1) > len(str2):
            str_ = str1
        elif len(str1) < len(str2):
            str_ = str2
        else:
            str_ = min(str1,str2)
    dp[(m,n,str_)] = str_      
    return str_

def lcs_tabulation(nums1, nums2, m, n):
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]
    str_ = ""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if nums1[i-1] == nums2[j-1]:
                str_ = dp[i-1][j-1]
                str_ += nums1[i-1]
            else:
                str1 = dp[i-1][j]
                str2 = dp[i][j-1]
                if len(str1) > len(str2):
                    str_ = str1
                elif len(str1) < len(str2):
                    str_ = str2
                else:
                    str_ = min(str1,str2)
            dp[i][j] = str_
    return dp[m][n]
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    dp = {}
    str_ = ""
    # return lcs_memoization(s1, s2, n, m, dp, str_)
    return lcs_tabulation(s1, s2, n, m)
