
//baekjoon source = "https://www.acmicpc.net/problem/2304"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class _2304_â��ٰ��� {

	static int n;
	static Integer[][] arr;
	static StringTokenizer st;
	static int[][] c;
	static int top = 0;

	static void solution(int check, int depth, int h) {
		
		for (int i = depth + 1; i < n - 1; i++) {
			if (arr[i][1] >= arr[depth][1]) {
				if (check == 0) {
					c[++top][0] = arr[i][0];
					c[top][1] = arr[i][1];
					solution(0, i, arr[i][1]);
					break;
				} else {
					return;
				}
			} else {
				solution(1, depth + 1, arr[i][1]);
			}
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(br.readLine());
		arr = new Integer[n][2];
		c = new int[n][2];
		
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		c[0][0] = arr[0][0];c[0][1] = arr[0][1];
		

		Arrays.sort(arr, new Comparator<Integer[]>() {
			@Override
			public int compare(Integer[] o1, Integer[] o2) {
				Integer a = o1[0];
				Integer b = o2[0];
				return a.compareTo(b);
			}
		});

		for (Integer[] i : arr) {
			System.out.println(Arrays.toString(i));
		}
		System.out.println();

		solution(0, 0, 0);
		c[++top][0] = arr[n-1][0];
		c[top][1] = arr[n-1][1];
		
		for (int[] i : c) {
			System.out.println(Arrays.toString(i));
		}
		
		int result = 0;
		for(int i = 0; i<top; i++) {
			
		}
	}
}
