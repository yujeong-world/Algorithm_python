import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        List<Double> list = new ArrayList<>();

        for(int i=0; i<n; i++){
            Double score = sc.nextDouble();
            list.add(score);
        }

        //최대값 구하기
        Double m = Collections.max(list);

        Double sum=0.0;
        // 새로운 점수를 만들기
        for (int i =0; i< list.size(); i++){
            double change = ((list.get(i)/m)*100);
            list.set(i, change);
            sum += list.get(i);
        }

        // 평균 구하기
        double avg = (sum / n);
        System.out.println(avg);

    }
}