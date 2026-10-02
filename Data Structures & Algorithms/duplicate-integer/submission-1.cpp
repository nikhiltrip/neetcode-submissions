#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> a;
        for(int i=0; i<nums.size(); i++)
            a.insert(nums[i]);
        if(a.size() != nums.size())
            return true;
        return false;
    }
};
