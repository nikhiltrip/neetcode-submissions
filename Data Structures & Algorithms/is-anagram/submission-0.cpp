#include <unordered_map>
#include <string>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> pairs_s;
        std::unordered_map<char, int> pairs_t;
        if(s.size() != t.size())
            return false;
        for(int i=0; i<s.size(); i++){
            if(pairs_s[s[i]] != 0)
                pairs_s[s[i]]++;
            else pairs_s[s[i]] = 1;
            if(pairs_t[t[i]] != 0)
                pairs_t[t[i]]++;
            else pairs_t[t[i]] = 1;
        }
        for(int i=0; i<s.size(); i++){
            if(pairs_s[s[i]] != pairs_t[s[i]])
                return false;
        }
        return true;
    }
};
