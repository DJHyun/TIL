//baekjoon source = "https://www.acmicpc.net/problem/2447"
package f_ÇÔ¼ö;

import java.io.IOException;
import java.util.Scanner;

public class º°Âï±â_10_2447 {

	static Scanner sc = new Scanner(System.in);
	static int n = sc.nextInt();
	static int[][] visited = new int[n][n];

	static String solution(int x, int y) {
		while (x != 0 || y != 0) {
			if (visited[x][y] == 1) {
				return " ";
			}
			if (x % 3 == 1 && y % 3 == 1) {
				if (visited[x][y] == 0) {
					visited[x][y] = 1;
				}
				return " ";
			}
			x /= 3;
			y /= 3;
		}
		return "*";
	}

	public static void main(String[] args) throws IOException {

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i == 0 || i == n - 1 || i == 2 || i == n-3 || i == 6 || i== n-7 || j == 2) {
					System.out.print("*");
				} else {
					System.out.print(solution(i, j));
				}
			}
			if (i != n - 1) {
				System.out.println();
			}
		}
	}
}
