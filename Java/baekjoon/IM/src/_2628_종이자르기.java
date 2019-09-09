//baekjoon source = "https://www.acmicpc.net/problem/2628"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2628_�����ڸ��� {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int y = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken());
		int[][] arr = new int[2 * x-1][2 * y-1];
		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			if (st.nextToken().equals("0")) {
				int a = Integer.parseInt(st.nextToken());
				int b = 1+(a-1)*2;
				for (int j = 0; j < y * 2 -1; ++j) {
					arr[b][j] = 1;
				}
			} else {
				int a = Integer.parseInt(st.nextToken());
				int b = 1+(a-1)*2;
				for (int j = 0; j < x * 2 -1; ++j) {
					arr[j][b] = 1;
				}
			}

		}
		

		int xr = 0, xResult = 0;
		for (int i = 0; i < 2 * x -1; ++i) {
			if (arr[i][0] == 0) {
				xr++;
			} else {
				xResult = Math.max(xr, xResult);
				xr = 0;
			}
		}
		xResult = Math.max(xr, xResult);

		int yr = 0, yResult = 0;
		for (int i = 0; i < 2 * y -1; ++i) {
			if (arr[0][i] == 0) {
				yr++;
			} else {
				yResult = Math.max(yResult, yr);
				yr = 0;
			}
		}
		yResult = Math.max(yResult, yr);
		
		xResult = xResult/2+1;
		yResult = yResult/2+1;
		bw.write(xResult* yResult+ "");
		bw.flush();
	}
}
