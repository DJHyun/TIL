//baekjoon source = "https://www.acmicpc.net/problem/3085"
package 브루트포스;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 사탕게임_3085 {
	
	static int n;
	static String[][] arr;
	
	
	
	
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		n = Integer.parseInt(br.readLine());
		arr = new String[n][n];
		
		for(int i = 0 ; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String[] s = st.nextToken().split("");
			for(int j = 0; j<n; j++) {
				arr[i][j] = s[j];
			}
		}
		
		for(String[] s : arr) {
			System.out.println(Arrays.toString(s));
		}
		
		
	}
}
