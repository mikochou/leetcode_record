//直接用把x转换为回文然后对比，如果数很大的话在c++会超时。所以使用双指针。
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int fast=x,slow=x,rhalf=0;
        while(fast/10){
            rhalf = rhalf*10 + slow%10;
            slow /= 10;
            fast /= 100;
        }
        return fast==0?rhalf==slow:slow/10==rhalf;
    }
};