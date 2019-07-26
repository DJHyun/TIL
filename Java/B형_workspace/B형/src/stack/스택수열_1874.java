// baekjoon source = "https://www.acmicpc.net/problem/1874"
package stack;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class 스택수열_1874 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<>();

		StringBuilder result = new StringBuilder();
		StringBuilder pro = new StringBuilder();
		int[] num = new int[n * 2];
		int stan = 1, top = -1;
		for (int i = 1; i <= n; i++) {
			int check = Integer.parseInt(br.readLine());
			pro.append(check);
			for (int j = stan; j <= check; j++) {
				stack.push(j);
				num[++top] = 1;
				stan++;
			}
			result.append(stack.pop());
			num[++top] = 0;
		}
		
		if (pro.toString().equals(result.toString())) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < n * 2; i++) {
				sb.append((num[i] == 1 ? "+" : "-") + "\n");
			}
			bw.write(sb + "");
		} else {
			bw.write("NO");
		}
		bw.flush();
	}
}
