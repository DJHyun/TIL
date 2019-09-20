//sw expert source = "www.swexpertacademy.com/7985"
package D3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _7985_RootedBinaryTree¿Á±∏º∫ {
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("src/D3/input.txt"));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc<=T; ++tc) {
			int k = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] score = new int[(int)Math.pow(2,k)-1];
			for(int i = 0; i<(int)Math.pow(2,k)-1; ++i) {
				score[i] = Integer.parseInt(st.nextToken());
			}
			System.out.println(Arrays.toString(score));
			
			Queue<Integer> q = new LinkedList<>();
			q.add(0);q.add(((int)Math.pow(2, k)-1)/2);q.add((int)Math.pow(2, k)-1);
			bw.write(String.format("#%d ", tc));
			while (!q.isEmpty()) {
				int len = q.size();
				for (int i = 0; i<len; ++i) {
					
					bw.write("qqqq"+" "+q);
					System.out.println(q+" "+len);
					int left = q.poll();
					int mid = q.poll();
					int right = q.poll();
					bw.write(score[mid]+" ");
					bw.write("asdfasdf "+left+" "+mid+" "+right+" ");
					if (left < mid && mid < right) {
						int tmp = right;
						right = mid;
						mid = (left+right)/2;
						q.add(left);q.add(mid);q.add(right);
						left = right;
						right = tmp;
						mid = (left+right)/2;
						q.add(left);q.add(mid);q.add(right);
					}
				}
				bw.newLine();
				bw.write(q.size()+"");
			}
		}
		bw.flush();
	}
}
