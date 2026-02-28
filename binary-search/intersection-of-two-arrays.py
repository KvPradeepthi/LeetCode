class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for i in nums1:
            if i in nums2:
                lst.append(i)
        sets=set(lst)
        return list(sets)
        