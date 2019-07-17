//sw expert source = "www.swexpertacademy.com/7466"
package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 팩토리얼과최대공약수_7466 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			String[] st = br.readLine().split(" ");
			long n = Integer.parseInt(st[0]);
			long k = Integer.parseInt(st[1]);


			long result = 1;
			if (n >= k) {
				result = k;
			} else {
				for (long i = n; i > 0; i--) {
					if (k % i == 0) {
						result *= i;
						k /= i;
					}
				}
			}
			System.out.println(result);
		}
	}
}
