//baekjoon source = "https://www.acmicpc.net/problem/6064"
package h_수학_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 카잉달력_6064 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());

		for (int T = 0; T < t; T++) {
			String[] st = br.readLine().split(" ");
			int m = Integer.parseInt(st[0]), n = Integer.parseInt(st[1]), x = Integer.parseInt(st[2]),
					y = Integer.parseInt(st[3]);

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
					System.out.println(check);
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
			bw.write(String.valueOf(result) + "\n");
			bw.flush();
		}
	}
}
