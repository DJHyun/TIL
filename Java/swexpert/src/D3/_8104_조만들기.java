//sw expert source = "www.swexpertacademy.com/8104"
package D3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _8104_조만들기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc<=T; ++tc) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			int[] arr = new int[k];
			boolean flag = true;
			
			for (int i = 1; i<=n*k; ++i) {
				if (flag) {
					if (i%k == 0) {
						arr[k-1] += i;
						flag = false;
					}else {
						arr[i%k-1] += i;
					}
				}else {
					
					if (i%k == 0) {
						arr[0] += i;
						flag = true;
					}else {
						arr[k-i%k] += i;
					}
				}
			}
			
			sb.append("#"+tc+" ");
			for(int i = 0; i<k; ++i) {
				sb.append(arr[i]+" ");
			}
			sb.append("\n");
		}
		bw.write(sb+"");
		bw.flush();
	}
}
