//baekjoon source = "https://www.acmicpc.net/problem/2675"
package g_���ڿ�;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ���ڿ��ݺ�_2675 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			String[] st = br.readLine().split(" ");
			int r = Integer.parseInt(st[0]);
			String ns = "";
			for(int i = 0; i<st[1].length(); i++) {
				for(int j = 0; j<r; j++) {
					ns += st[1].charAt(i);
				}
			}
			bw.write(ns+"\n");
		}
		bw.flush();
	}
}
