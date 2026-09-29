#counter->dict mappin w count
#most_common(k),k->list len for common
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        return [key for key,value in count_dict.most_common(k)]
        