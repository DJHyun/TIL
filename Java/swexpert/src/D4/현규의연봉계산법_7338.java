//sw expert source = "www.swexpertacademy.com/7338"
package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 현규의연봉계산법_7338 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			String[] st = br.readLine().split(" ");
			long y = Long.parseLong(st[0]), m = Long.parseLong(st[1]);
			long a = y - 2016;
			long mok = a / 13, na = a % 13;
			y -= mok;
			if (m - na <= 0) {
				m = 13 - (na-m);
				y -= 1;
			}else {
				m -= na;
			}
			System.out.println("#" + test_case + " " + y + " " + m);


		} // end of test_case
	}
}
