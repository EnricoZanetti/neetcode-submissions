class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        
        already_checked = []
        for el in sorted_nums:
            if el in already_checked:
                return True
            already_checked.append(el)
        
        return False
