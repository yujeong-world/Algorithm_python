import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        //집합 선언
        HashSet set = new HashSet();

        for (int i=0; i<10; i++){
            int num = sc.nextInt();
            //집합에 담는다.
            num = num % 42;
            set.add(num);
        }
        System.out.println(set.stream().count());
    }
}