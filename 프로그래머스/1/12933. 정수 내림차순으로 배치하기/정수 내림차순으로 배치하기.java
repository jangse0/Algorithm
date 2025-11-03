import java.util.*;

class Solution {
    public long solution(long n) {
        String str = String.valueOf(n);
        char[] arr = str.toCharArray();
        
        Arrays.sort(arr);
        
        StringBuilder re_arr = new StringBuilder(new String(arr));
        re_arr.reverse();
        
        return Long.parseLong(re_arr.toString());
    }
}