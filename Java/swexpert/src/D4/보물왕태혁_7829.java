//sw expert source = "www.swexpertacademy.com/7829"
package D4;

import java.util.Scanner;

public class º¸¹°¿ÕÅÂÇõ_7829 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();

		for (int test_case = 1; test_case <= t; test_case++) {
			int p = sc.nextInt();
			sc.nextLine();
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;
			for (int i = 0; i < p; i++) {
				int n = sc.nextInt();
				if (max < n) {
					max = n;
				}
				if (min > n) {
					min = n;
				}
			}
			
			System.out.printf("#%d %d%n",test_case,max*min);
		}
	}
}
