import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 통화 횟수 입력
        int a = sc.nextInt();

        // 통화 시간을 저장할 배열
        int[] call = new int[a];

        // 통화 시간을 입력 받음
        for (int i = 0; i < a; i++) {
            call[i] = sc.nextInt();
        }

        int yFee = 0;
        int mFee = 0;

        // 요금 계산
        for (int i = 0; i < a; i++) {
            // 영식 요금 : 30초마다 10원
            yFee += ((call[i] / 30) + 1) * 10;

            // 민식 요금 : 60초마다 15원
            mFee += ((call[i] / 60) + 1) * 15;
        }

        // 더 저렴한 요금제 선택 및 출력
        if (yFee < mFee) {
            System.out.printf("Y %d\n", yFee);
        } else if (mFee < yFee) {
            System.out.printf("M %d\n", mFee);
        } else {
            System.out.printf("Y M %d\n", yFee);
        }
    }
}