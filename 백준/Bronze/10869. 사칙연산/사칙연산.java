import java.util.*;
import java.io.*;
class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        //입력 받기
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        
        //덧셈
        System.out.println(A+B);
        //뺄셈
        System.out.println(A-B);
        //곱셈
        System.out.println(A*B);
        //나눗셈(몫)
        System.out.println(A/B);
        //나머지
        System.out.println(A%B);
        
    }
}