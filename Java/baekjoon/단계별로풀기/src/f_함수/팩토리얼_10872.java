//baekjoon source = "https://www.acmicpc.net/problem/10872"
package f_�Լ�;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ���丮��_10872 {
	static int result = 1;

	static void fact(int a) {
		if (a <= 1) {
			return;
		}

		result *= a;
		fact(a - 1);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		fact(Integer.parseInt(br.readLine()));
		System.out.println(result);
	}
}
