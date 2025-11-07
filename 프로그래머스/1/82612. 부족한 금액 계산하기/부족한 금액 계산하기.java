class Solution {
    public long solution(int price, int money, int count) {
        long total_price = 0;
        for(int i=1; i<=count; i++){
            total_price += i*price;
        }
        
        if(total_price<=money)
            return 0;
        else
            return (total_price-money);
    }
}