class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        char[] str = s.toCharArray();
        for(int i=0; i<str.length; i++){
            int count = 0;
            for (int j=0; j<i; j++){
                if(str[i]==str[j]){
                    count= Math.abs(j-i);
                }
            }
            if(count==0){
                count=-1;
            }
            answer[i]=count;
        }
        return answer;
    }
}