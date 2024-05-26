import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] arr = new int[7];

        //입력 받는다.
        for(int i=0; i<7; i++){
            arr[i] = sc.nextInt();
        }

        // 홀수만 뽑아내기
        List<Integer> list = new ArrayList<>();

        for(int i=0; i<7; i++){
            if(arr[i] % 2 != 0 ){
                list.add(arr[i]);
            }
        }

        int sum = 0;

        //홀수가 존재하지 않는 경우

        // 홀수의 합
        for(int i=0; i<list.size(); i++){
            sum += list.get(i);
        }


        if(sum == 0){
            System.out.println(-1);
        }else {
            int min = list.get(0);
            for(int i=0; i<list.size(); i++){
                // 가장 작은 홀수
                if(list.get(i) < min){
                    min = list.get(i);
                }
            }
            System.out.println(sum);
            System.out.println(min);
        }

    }
}