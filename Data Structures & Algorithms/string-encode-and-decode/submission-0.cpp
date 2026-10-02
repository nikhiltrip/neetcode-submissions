class Solution {
public:

    string encode(vector<string>& strs) {
        string s = "";
        for(string str : strs){
            s += to_string(str.size()) + '#' + str;
        }
        return s;
    }

    //4#neet4#code4#love4#you -> neet, code, love, you
    vector<string> decode(string s) {
        vector<string> strs;
        int i = 0;
        while(i < s.size()){
            int j = i;
            while(s[j] != '#') j++;
            int length = stoi(s.substr(i, j - i));
            string str = s.substr(j+1, length);
            strs.push_back(str);
            i = j + length + 1;
        }
        return strs;
    }
};
