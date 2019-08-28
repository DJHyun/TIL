//baekjoon source = "https://www.acmicpc.net/problem/2578"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2578_���� {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int[][] arr = new int[5][5];
		StringTokenizer st;
		for (int i = 0; i < 5; ++i) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; ++j) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] x = new int[] { 5, 5, 5, 5, 5 };
		int[] y = new int[] { 5, 5, 5, 5, 5 };
		int[] z = new int[] { 5, 5 };
		int cnt = 0, result = 0;

		boolean total_flag = false;
		for (int i = 0; i < 5; ++i) {
			st = new StringTokenizer(br.readLine());
			boolean mid_flag = false;
			for (int j = 0; j < 5; ++j) {
				
				result++;
				int check = Integer.parseInt(st.nextToken());
				boolean flag = false;
				
				for (int a = 0; a < 5; ++a) {
					for (int b = 0; b < 5; ++b) {
						if (arr[a][b] == check) {
							x[b]--;
							if (x[b] == 0) cnt++;
							y[a]--;
							if (y[a] == 0) cnt++;
							if (a == b) {
								z[0]--;
								if (z[0] == 0) cnt++;
							}
							if (a == 0 && b == 4 || a == 1 && b == 3 || a == 2 && b == 2 || a == 3 && b == 1 || a == 4 && b == 0 ) {
								z[1]--;
								if (z[1] == 0) cnt++;
							}
							flag = true;
							if (cnt >= 3) {
								total_flag = true;
								mid_flag = true;
							}
							break;
						}
					}
					if (flag) break;
				}
				if (mid_flag) break;
			}
			if (total_flag) break;
		}
		bw.write(result+"");
		bw.flush();
	}
}
