//sw expert source = "www.swexpertacademy.com/7854"
package D4;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class ÃÖ¾à¼ö_7854 {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
//			String n = sc.next();
//			int k = n.length();
//			int cnt = 0;
//			boolean flag = false;
//
//			for (int i = 1; i <= k; i++) {
//				long st = (long) Math.pow(10, i - 1);
//				long en = (long) Math.pow(10, i);
//				
//				for (long j = st + 1; j <= en; j++) {
//					if (j > Long.parseLong(n)) {
//						flag = true;
//						break;
//					}
//					if (en % j == 0) {
//						cnt++;
//					}
//				}
//				if (flag) {
//					break;
//				}
//			}
//			System.out.println(cnt + 1);

			long n = sc.nextLong();
			int cnt = 0;
			Map map = new HashMap();
			long check = (long) Math.pow(10, 9);
			for (long i = 1; i <= Math.sqrt(check); i++) {
				if (i > n) {
					break;
				}
				if (map.containsKey(i)) {
					continue;
				}
				if (check % i == 0) {
					if ((long) Math.pow(10, Long.toString(i).length()) % i == 0) {
						cnt++;
						map.put(i, 1);
						if (check/i < n && (long) Math.pow(10, Long.toString(check/i).length()) % (check/i) == 0) {
							cnt++;
							map.put(check/i, 1);
						}
					}
				}
			}
			System.out.println(cnt);
		}
	}
}