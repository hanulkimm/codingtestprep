import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n!=1) {
            int i = 2;
            while (n>1) {
                if (n%i==0) {
                    n/=i;
                    System.out.println(i);
                } else {
                    i += 1;
                }
            }
        }
    }
}

