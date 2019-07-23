//sw expert source = "www.swexpertacademy.com/7333"
package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 한솔이의택배아르바이트_7333 {
	static int n;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			n = Integer.parseInt(br.readLine());
			int[] box = new int[n];
			for (int i = 0; i < n; i++) {
				box[i] = Integer.parseInt(br.readLine());

			}

			Arrays.sort(box);
			int result = 0;
			int st = 0, rear = n - 1;
			while (true) {
				int i = 1;
				for (i = 1;; i++) {
					if (box[rear] * i >= 50) {
						break;
					}
				}
				
				
				rear--;
				st += (i - 1);
				result++;
				if (st > rear) {
					if (st - rear > 1) {
						result--;
					}
					break;
				}
			}

			System.out.printf("#%d %d%n", t, result);
		} // end of test_case
	}
}
