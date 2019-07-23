//sw expert source = "www.swexpertacademy.com/7393"
package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class ´ë±ÔÀÇÆÒ´ýÈ°µ¿_7393_¹Ì¿Ï {
	static int n,cnt;
	static int[][] arr;
	static int[] visited;

	static void dfs(int v, int depth, String s) {
		System.out.println(v + " " + depth + " " + s);
		visited[v] = 1;

		if (depth == n) {
			System.out.println("final  " + s);
			cnt++;
			return;
		}

		for (int i = 0; i < arr[v].length; i++) {
//			if (visited[arr[v][i]] == 0) {
			dfs(arr[v][i], depth + 1, s + Integer.toString(arr[v][i]));
//				visited[arr[v][i]] = 0;
//			}
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		arr = new int[10][2];
		arr[0] = new int[] { 1 };
		arr[9] = new int[] { 8 };
		for (int i = 1; i < 9; i++) {
			arr[i] = new int[] { i - 1, i + 1 };
		}
		for (int[] s : arr) {
			System.out.println(Arrays.toString(s));
		}
		for (int t = 1; t <= T; t++) {
			cnt = 0;
			n = Integer.parseInt(br.readLine());
			for (int i = 1; i < 10; i++) {
				visited = new int[10];
				System.out.println(i);
				dfs(i, 1, Integer.toString(i));
			}
			System.out.println("#"+t+" "+cnt);
		}
	}
}
