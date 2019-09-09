//baekjoon source = "https://www.acmicpc.net/problem/2750"
package k_����;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _2750_�������ϱ� {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int[] result = new int[n];
		for(int i = 0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			result[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(result);
		for(int i : result) {
			bw.write(i+"\n");
		}
		bw.flush();
	}
}
