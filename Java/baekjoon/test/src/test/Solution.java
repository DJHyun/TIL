package test;

import java.util.Scanner;

class Solution {
	static int[][] map;
	static boolean[][] visit;
	public static void main(String args[]) throws Exception {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			int N = sc.nextInt();
			map = new int[N][N];
			visit = new boolean [N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j]=sc.nextInt();
				}
			}
			
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(visit[i][j]==false) solve(map);
				}
			}
			
			System.out.println("#" + test_case);
		}

		sc.close(); // ����� ���� ��ĳ�� ��ü�� �ݽ��ϴ�.
	}
	private static void solve(int[][] map2) {
		
		
	}
}
