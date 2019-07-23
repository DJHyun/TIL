//sw expert source = "www.swexpertacademy.com/7854"
package D4;

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
//			long[] check = new long[(int) Long.parseLong(n)+1];
//			boolean flag = false;
//			
//			for (int i = 1; i <= k; i++) {
//
//				long en = (long) Math.pow(10, i);
//				
//				for (long j = 1; j <= Math.sqrt(en); j++) {
//					System.out.println(j);
//					if (j > Long.parseLong(n)) {
//						flag = true;
//						break;
//					}
//					if (en % j == 0) {
//						if(Long.toString(j).length() == i) {
//							if(check[(int)j] == 0) {
//								cnt++;
//								check[(int)j] = 1;
//							}
//						}
//						
//						if (Long.parseLong(n) > en / j) {
//							if(check[(int)(en/j)] == 0) {
//								cnt++;
//								check[(int)(en/j)] = 1;
//							}
//						}
//					}
//				}
//				if (flag) {
//					break;
//				}
//			}
//			System.out.println(cnt);
//			for(int i = 0 ; i<check.length; i++) {
//				System.out.println(i + " "+check[i]);
//			}

			long n = sc.nextLong();
			int k = Long.toString(n).length();
			for (int i = 1; i < 10; i++) {
				if (Math.pow(10, i) == n) {
					k--;
				}
			}
			int cnt = 0;
			long check = (long) Math.pow(10, k);
			for (long i = 1; i <= Math.sqrt(check); i++) {
				if (i > n) {
					break;
				}
				if (check % i == 0) {
					if (Math.pow(10, Long.toString(i).length()) % i == 0) {
						cnt++;
					}
					if (i != (check / i) && n >= (check / i)
							&& Math.pow(10, Long.toString(check / i).length()) % (check / i) == 0) {
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}
	}
}