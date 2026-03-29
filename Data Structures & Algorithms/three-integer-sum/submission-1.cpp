class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int left, right, sum;
        std::sort(nums.begin(), nums.end());
        int len = nums.size();
        vector<vector<int>> result = {};
        for (int i = 0; i < len - 2; ++i)
        {
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            left = i + 1;
            right = len - 1;
            while (left < right){
                sum = nums[i] + nums[left] + nums[right];
            
                if (sum == 0){
                    result.push_back({nums[i], nums[left], nums[right]});

                    while (left < right && nums[left] == nums[left+1]){
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right-1]){
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                }
                else if (sum < 0){
                    left += 1;
                } else {right -= 1;}
            }
        }
        return result;
    }
};
