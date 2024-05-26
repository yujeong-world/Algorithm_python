import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        //수열
        List<Integer> list = new ArrayList<>();

        for(int i=1; i<1000; i++){
            for(int j=1; j<=i; j++){
                list.add(i);
            }
        }

        int sum = 0;
        // 구간의 합 출력
        for(int i = a-1; i<b; i++){
            sum += list.get(i);
        }
        System.out.println(sum);

    }
}