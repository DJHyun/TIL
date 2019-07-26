// baekjoon source = "https://www.acmicpc.net/problem/2493"
package stack;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class ž_2493 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for(int i = 0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		for(int i = n-1; i>0; i--) {
			boolean flag = true;
			for(int j = i-1; j>-1; j--) {
				if (arr[i] < arr[j]) {
					arr[i] = j+1;
					flag = false;
					break;
				}
			}
			if(flag) {
				arr[i] = 0;
			}
		}
		arr[0] = 0;
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i<n; i++) {
			sb.append(arr[i]+" ");
		}
		bw.write(sb+"");
		bw.flush();
	}
}
