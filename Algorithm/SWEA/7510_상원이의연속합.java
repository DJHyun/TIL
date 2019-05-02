// SW Expert Academy
import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			int result = 0;

			for (int i = 1; i <= n; i++) {
				int check = 0;
				for (int j = i; j <= n; j++) {
					check += j;
					if (check > n) {
						break;
					} else if (check == n) {
						result++;
						break;
					}
				}
			}
			System.out.printf("#%d %d %n",test_case,result);
		}
	}
}