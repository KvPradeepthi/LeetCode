class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp={}
        s=0
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        max_freq=0
        ans=0
        for key in mp:
            if mp[key]>max_freq:
                max_freq=mp[key]
                ans=key
        return ans  