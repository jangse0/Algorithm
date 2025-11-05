class Solution {
    public boolean solution(int x) {
        boolean answer;
        int sum = 0;
        char[] arr_x = String.valueOf(x).toCharArray();
        
        for(char c:arr_x){
            sum+=c-'0';
        }
        
        if(x%sum==0){
            answer = true;
        }
        else
            answer = false;
        
        return answer;
    }
}