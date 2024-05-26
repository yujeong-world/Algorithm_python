import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i=1; i<=n; i++){
            for(int j=n-i; j>0; j--){
                System.out.printf(" ");
            }
            for(int p=0; p<i; p++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}