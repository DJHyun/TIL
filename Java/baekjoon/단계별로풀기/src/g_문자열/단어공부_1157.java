//baekjoon source = "https://www.acmicpc.net/problem/1157"
package g_���ڿ�;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class �ܾ����_1157 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int[] arr = new int[26];

		String s = br.readLine();
		s = s.toUpperCase();
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < s.length(); i++) {
			int check = (int) s.charAt(i) - 65;
			arr[check]++;
			max = Math.max(max, arr[check]);
		}
		boolean flag = true;
		boolean reF = true;
		String result = "";
		for (int i = 0; i < 26; i++) {
			if(arr[i] == max) {
				if (flag) {
					flag = false;
					result = Character.toString((char)(i+65));
				}else {
					bw.write("?");
					reF = false;
					break;
				}
			}
		}
		if (reF) {
			bw.write(result);
		}
		bw.flush();
	}
}
