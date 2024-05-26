import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        //배열의 개수 입력받기
        int n = sc.nextInt();

        int[][] arr = new int[n][10];

        for (int i=0; i<n; i++){
            for (int j=0; j<10; j++){
                arr[i][j] = sc.nextInt();
            }
            Arrays.sort(arr[i]);
        }

        //배열에서 3번째 큰 값 출력
        for (int i=0; i<n; i++){
            System.out.println(arr[i][7]);
        }

    }
}