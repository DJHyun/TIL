//sw expert source = "www.swexpertacademy.com/7701"
package D4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ¿°¶ó´ë¿ÕÀÇÀÌ¸§Á¤·Ä_7701 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int n = Integer.parseInt(br.readLine());
			Set<String> set = new HashSet<>();
			
			Comparator<String> ct = new Comparator<String>() {

				@Override
				public int compare(String o1, String o2) {
					// TODO Auto-generated method stub
					return o1.length() - o2.length();
				}

			};
			for (int i = 0; i < n; i++) {
				set.add(br.readLine());
			}
			List<String> list = new ArrayList<>(set);
			Collections.sort(list);
			Collections.sort(list, ct);
			bw.write("#"+t);
			bw.newLine();
			for(int i = 0; i<list.size(); i++) {
				bw.write(list.get(i));
				bw.newLine();
			}
		}
		bw.flush();
	}
}
