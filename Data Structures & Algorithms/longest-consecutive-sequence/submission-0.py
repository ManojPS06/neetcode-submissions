class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sort_list = sorted(set(nums))
        longest = 1
        current = 1

        for i in range(1, len(sort_list)):
            if sort_list[i] - sort_list[i - 1] == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1

        return longest