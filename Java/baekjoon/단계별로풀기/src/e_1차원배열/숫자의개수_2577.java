//baekjoon source = "https://www.acmicpc.net/problem/2577"
package e_1�����迭;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class �����ǰ���_2577 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] check = new int[10];
		int a = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
		
		for(int i = 0; i<Integer.toString(a).length(); i++) {
			check[Integer.toString(a).charAt(i) - '0'] ++ ;
		}
		for(int i : check) {
			System.out.println(i);
		}
	}
}
