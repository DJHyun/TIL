// baekjoon source = "https://www.acmicpc.net/problem/2905"
package queue;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.MaximizeAction;

public class 홍준이와울타리_2905_미완 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		int[] result = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			result[i] = arr[i];
		}

		int one = 0, two = 0, index = 0, c = 0;
		while (index + x <= n) {
			int min = Integer.MAX_VALUE;
			for (int i = index; i < index + x; i++) {
				min = Math.min(min, arr[i]);
			}
			for (int i = index; i < index + x; i++) {
				result[i] -= min;
				if (result[i] == 0) {
					c = i ;
				}
			}
			index = c;
			one++;
		}
		for (int i : result) {
			if (i > 0)
				two += i;
		}
		bw.write(two + "\n");
		bw.write(one + "");
		bw.flush();

	}
}
