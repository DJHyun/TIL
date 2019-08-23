//baekjoon source = "https://www.acmicpc.net/problem/2116"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2116_�ֻ����ױ� {

	static int n;
	static int[][] arr;
	static int answer = 0;

	static void solution(int x, int depth, int sum) {
		if (depth == n) {
			answer = Math.max(answer, sum);
			return;
		}

		int result = 0;
		for (int i = 0; i < 6; i++) {
			if (x == 0 || x == 5) {
				if (i == 0 || i == 5)
					continue;
				result = Math.max(result, arr[depth][i]);
			} else if (x == 1 || x == 3) {
				if (i == 1 || i == 3)
					continue;
				result = Math.max(result, arr[depth][i]);
			} else {
				if (i == 2 || i == 4)
					continue;
				result = Math.max(result, arr[depth][i]);
			}
		}
		sum += result;
		if (depth == n - 1) {
			solution(0, depth + 1, sum);
			return;
		}
		for (int i = 0; i < 6; ++i) {
			if (arr[depth + 1][i] == arr[depth][x]) {
				switch (i) {
				case 0:
					solution(5, depth + 1, sum);
					break;
				case 1:
					solution(3, depth + 1, sum);
					break;
				case 2:
					solution(4, depth + 1, sum);
					break;
				case 3:
					solution(1, depth + 1, sum);
					break;
				case 4:
					solution(2, depth + 1, sum);
					break;
				case 5:
					solution(0, depth + 1, sum);
					break;
				}
				break;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(br.readLine());
		arr = new int[n][6];
		StringTokenizer st;
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 6; ++j) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < 6; ++i) {
			solution(i, 0, 0);
		}
		bw.write(answer + "");
		bw.flush();
	}
}
