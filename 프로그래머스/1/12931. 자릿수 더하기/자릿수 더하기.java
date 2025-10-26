import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int len = 0;
        
        len = Integer.toString(n).length();
        
        for (int i = 1; i < len; i++){
            answer+= n/(Math.pow(10, i));
            
        }

        return answer;
    }
}