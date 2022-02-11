class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        run_sum, count = 0, 0
        run_sums = defaultdict(int)
        run_sums[run_sum] += 1
        
        for num in nums:
            run_sum += num
            
            count += run_sums[run_sum - k]
            run_sums[run_sum] += 1
        return count