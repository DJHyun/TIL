//baekjoon source = "https://www.acmicpc.net/problem/6064"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 카잉달력_6064 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());

		for (int T = 0; T < t; T++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken()), n = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken()),
					y = Integer.parseInt(st.nextToken());

			int d = m - n;
			int check = x;
			if (check > n) {
				check %= n;
				if (check == 0) {
					check = 1;
				}
			}
			int result = x;

			if (d > 0) {
				int c = check;
				while (true) {
					if (check == y) {
						break;
					}
					check += d;
					if (check > n) {
						check %= n;
						if (check == 0) {
							check = 1;
						}
					}
					if (check == c) {
						result = -1;
						break;
					}
					result += m;
				}
			} else if (d < 0) {
				int c = check;
				while (true) {
					if (check == y) {
						break;
					}
					check += d;
					if (check < 1) {
						check += n;
					}
					if (check == c) {
						result = -1;
						break;
					}
					result += m;
				}
			} else {
				result = x != y ? -1 : x;
			}
			bw.write(result + "\n");
			bw.flush();
		}
	}
}
