class Solution {
    public int[] solution(long n) {
        String num = String.valueOf(n);
        int len = num.length();
        int[] answer = new int[len];
        

        for (int i=0; i<len; i++){
            answer[i] = (int)(n % 10);
            n /= 10;
        }
        return answer;
    }
}