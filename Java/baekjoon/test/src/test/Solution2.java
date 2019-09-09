package test;


import java.util.Scanner;

class Solutio {
	static int[][] map;
	static int[] town;
	static int[] chk;
	static int N,ans;
	public static void main(String args[]) throws Exception {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			 N = sc.nextInt();
			ans=Integer.MAX_VALUE;
			map = new int[N][N]; //��������
			town = new int[N]; //������ �����ڼ� ����
			chk = new int[N]; // ������ 1,2
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j]=sc.nextInt();
				}
			}
			
			for(int i=0; i<N; i++){
				town[i]=sc.nextInt();
			}
			
			chk[0]=1;
			solve(0,chk);
			
			System.out.println("#" + test_case+" "+ans);
		}

		sc.close(); // ����� ���� ��ĳ�� ��ü�� �ݽ��ϴ�.
	}
	private static void solve(int idx, int[] chk2) {
		if(nozero(chk2)==true) { //�� �����Ϸ��
			ans= cal(chk2)<ans?cal(chk2):ans; //����ã��
			return;
		}
		for(int j=0; j<N; j++) {
			if(map[idx][j]==1) { //�������ִ� �����̸�
				chk2[j]=1;
				solve(j,chk2);
				chk2[j]=2;
				
			}
		}
		
	}
	private static boolean nozero(int[] arr) {
		boolean f = true;
		for(int i=0; i<arr.length; i++) {
			if(arr[i]==0) f=false;
			else continue;
		}
		return f;
	}
	private static int cal(int[] arr2) {
		int one = 0;
		int two = 0;
		for(int i=0; i<arr2.length; i++) {
			if(arr2[i]==1) one+=town[i];
			else two += town[i];
		}
		
		return Math.abs(one-two);
	}
	
}
