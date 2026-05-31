class Solution {
public:

    string encode(vector<string>& strs) {
        string ret = "" ;

        for (auto itr : strs) ret += itr + (char)'¶' ;

        return ret ; 
    }

    vector<string> decode(string s) {

        vector <string> ret ;

        if (s.size ())

        ret.push_back ("") ;

        for (int i = 0 ; i < s.length () ; i ++) {

            ret.back () += s [i] ;

            if (s [i] == (char)'¶') {

                ret.back ().pop_back () ;

                if (i != s.length () - 1) ret.push_back ("") ;
            }

        }

        return ret ;

    }
};
