//baekjoon source = "https://www.acmicpc.net/problem/10869"
package 입출력과사칙연산;

import java.util.Scanner;

public class 사칙연산_10869 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		
		System.out.println(a + b);
		System.out.println(a - b);
		System.out.println(a * b);
		System.out.println(a / b);
		System.out.println(a % b);
	}
}
