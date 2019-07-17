//baekjoon source = "https://www.acmicpc.net/problem/2292"
package h_¼öÇÐ_1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ¹úÁý_2292 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		long n = Long.parseLong(br.readLine());
		long idx = 1;
		while(true) {
			if(n <= (2 + (idx-1)*(6*idx))) {
				System.out.println(idx);
				break;
			}
			idx++;
		}
	}
}
