import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int ans = 0;
        for (int i = 1; i < n+1; i++) {
            ans +=i;
        }
        System.out.println(ans);
    }
}
