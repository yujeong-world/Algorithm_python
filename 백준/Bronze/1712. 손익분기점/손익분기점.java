import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        //개수
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int num = 1;
        // a + (b * 개수 ) / 170
        // 생산 비용 > 가격 * 개수
        if(c <=b){
            // 판매가격 보다 재료비가 비싼 경우 손익분기점 존재하지 않음
            num = -1;
            System.out.println(num);
        }else{
            num = (a/(c-b))+1;
            System.out.println(num);
        }

    }
}