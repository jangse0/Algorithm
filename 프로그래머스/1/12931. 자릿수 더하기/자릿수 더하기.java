import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int len = Integer.toString(n).length();

        for (int i = 0; i < len; i++){
            answer+= n%10;
            n /= 10;

        }

        return answer;
    }
}