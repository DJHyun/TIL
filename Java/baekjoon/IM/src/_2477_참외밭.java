
//baekjoon source = "https://www.acmicpc.net/problem/2477"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class _2477_���ܹ� {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[][] check = new int[][] { { 3, 1, 3, 1, 4, 2 }, { 4, 2, 4, 2, 3, 1 }, { 1, 4, 1, 4, 2, 3 },
				{ 2, 3, 2, 3, 1, 4 } };

		StringTokenizer st;
		List<int[]> list = new ArrayList<>();
		int[] c = new int[5];

		for (int i = 0; i < 6; ++i) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			c[a]++;
			list.add(new int[] { a, Integer.parseInt(st.nextToken()) });
		}
		
		boolean while_flag = true;
		while (while_flag) {
			for (int i = 0; i < 4; ++i) {
				boolean flag = true;
				for (int j = 0; j < 6; ++j) {
					if (check[i][j] != list.get(j)[0]) {
						flag = false;
						break;
					}
				}
				if (flag) {
					while_flag = false;
					break;
				}
			}
			if (while_flag) {
				int[] tmp = list.remove(0);
				list.add(tmp);
			}
		}
		bw.write((list.get(5)[1] * list.get(4)[1] - list.get(1)[1] * list.get(2)[1])*n+"");
		bw.flush();
	}
}
