//sw expert source = "www.swexpertacademy.com/8016"
package D3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class _8016_홀수피라미드 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int tc = 1; tc <= T; ++tc) {
			sb.append(String.format("#%d ", tc));
			long n = Long.parseLong(br.readLine());
			long result = (long) (1 + (n - 1) * ((2 *n) - 2));
			sb.append(result + " " + (result + 2 * ((2 * n - 1) - 1)) + "\n");
		}
		bw.write(sb + "");
		bw.flush();
	}
}
