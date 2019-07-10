//sw expert source = "www.swexpertacademy.com/7810"
package D4;

import java.util.Scanner;

public class 승현이의질문_7810 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test_case = sc.nextInt();
		for (int t = 1; t <= test_case; t++) {
			int n = sc.nextInt();
			sc.nextLine();
			String[] st = sc.nextLine().split(" ");
			int max = Integer.MIN_VALUE;
			for (int i = 0; i < n; i++) {
				max = Math.max(max, Integer.parseInt(st[i]));
			}
			int[] cnt = new int[max + 1];
			for (int i = 0; i < n; i++) {
				cnt[Integer.parseInt(st[i])]++;
			}

			int count = 0;
			for (int i = cnt.length - 1; i > -1; i--) {
				if (cnt[i] != 0) {
					count += cnt[i];
				}
				if (count >= i) {
					System.out.printf("#%d %d",t,i);
					break;
				}
			}

		}
	}
}
