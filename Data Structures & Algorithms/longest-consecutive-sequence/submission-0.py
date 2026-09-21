class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for x in nums:
            if x - 1 not in num_set:
                curr = x
                while curr + 1 in num_set:
                    curr += 1
                count = curr - x + 1
                if count > longest:
                    longest = count
        
        return longest