//SW Expert Academy
package _2일차;

import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class 롤러코스터 {
	static int [] check;
	static int result;
	static int[][] num;
	static void solut(int k, int depth, int[] arr) {
		if (k == depth) {
			System.out.println(Arrays.toString(arr));
			for(int i = 1; i<depth; ++i) {
				result = ((num[arr[i]-1][0]*result)+num[arr[i]-1][1]);
			}
			if (result == 1242) System.out.println(result);
			result = 1;
			return;
		}
		for (int i = 1; i < depth; ++i) {
			if (check[i] == 0) {
				arr[k] = i;
				check[i] = 1;
				solut(k+1,depth,arr);
				check[i] = 0;
			}
		}
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src/_2일차/롤러코스터_input.txt"));
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int test_case = 1; test_case <= t; ++test_case) {
			int n = sc.nextInt();
			result = 1;
			num = new int[n][2];
			int[] visited = new int[n+1];
			check = new int[n+1];
			for (int i = 0; i < n; ++i) {
				num[i][0] = sc.nextInt();
				num[i][1] = sc.nextInt();
			}

			for (int[] i : num) {
				System.out.println(Arrays.toString(i));
			}
			System.out.println();
			solut(1, n+1, visited);
		}

	}
}
