class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3
        counts = Counter(nums)

        return [x for x, count in counts.items() if count > threshold]