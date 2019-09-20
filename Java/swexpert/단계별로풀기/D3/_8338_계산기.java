//sw expert source = "www.swexpertacademy.com/8338"
package D3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _8338_°è»ê±â {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
				
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int test_case = 1; test_case <= t; ++test_case) {
			int n = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int result = 0;
			for (int i = 0; i<n; i++) {
				int number = Integer.parseInt(st.nextToken());
				if (i == 0) {
					result = number;
					continue;
				}
				
				if (i == 1) {
					if (result == 0 || result == 1) {
						result += number;
						continue;
					}
				}
				
				if (number == 1 || number == 0) {
					result += number;
				}else {
					if (result == 0 || result == 1) {
						result += number;
					}else {
						result *= number;
					}
				}
				
			}
			sb.append(String.format("#%d %d%n",test_case,result));
		}
		bw.write(sb+"");
		bw.flush();
	}
}
