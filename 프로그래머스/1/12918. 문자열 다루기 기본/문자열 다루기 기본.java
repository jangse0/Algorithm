import java.util.*;
class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        
        if(s.length()!=4 && s.length()!=6){
            return false;
        }
        
        List<String> list = new ArrayList<>();
        
        for(int i=0; i<s.length(); i++){
            list.add(s.substring(i, i+1));
        }
        
        for(String ss: list){
            try{
                Integer.parseInt(ss);
            }
            catch(NumberFormatException e){
                return false;
            }
        }
        
        
        return answer;
    }
}