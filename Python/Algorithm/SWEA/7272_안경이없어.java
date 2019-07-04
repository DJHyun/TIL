// SW Expert Academy
import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			String first = sc.next();
			String second = sc.next();
			String result = "SAME";

			String zero = "CEFGHIJKLMNSTUVWXYZ";
			String one = "ADOPQR";

			if (first.length() != second.length()) {
				result = "DIFF";
			} else {
				for (int i = 0; i < first.length(); i++) {
					if (zero.contains(Character.toString(first.charAt(i)))) {
						if (!zero.contains(Character.toString(second.charAt(i)))) {
							result = "DIFF";
							break;
						}
					} else if (one.contains(Character.toString(first.charAt(i)))) {
						if (!one.contains(Character.toString(second.charAt(i)))) {
							result = "DIFF";
							break;
						}
					}else {
						if(second.charAt(i) != 'B') {
							result = "DIFF";
							break;
						}
					}
				}
			}
			System.out.printf("#%d %s%n",test_case,result);
		}
	}
}