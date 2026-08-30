class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n=nums.size();
        int minIndex=0;
        int maxIndex=0;
        for (int i=0;i<n;i++)
        {
            if(nums[i]<nums[minIndex])
            {
                minIndex=i;
            }
            if(nums[i]>nums[maxIndex])
            {
                maxIndex=i;
            }
        }
        int a=minIndex;
        int b=maxIndex;
        if(a>b)
        {
            swap(a,b);
        }
        int option1=b+1;
        int option2=n-a;
        int option3=(a+1)+(n-b);

        int ans=min({option1,option2,option3});
        return ans;

        
    }
};