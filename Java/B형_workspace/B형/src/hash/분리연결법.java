package hash;

public class 분리연결법 {
	private class Entry {
		private int value;
		public Entry next;
	}

	private int size;
	private Entry[] hTable;

	public 분리연결법(int size) {
		this.size = size;
		this.hTable = new Entry[size];
	}

	public int hashMethod(int key) {
		return key % size;
	}

	public int getkey(int data) {
		return data;
	}

	public int add(int data) {
		int key = getkey(data);
		int hashValue = hashMethod(key);
		
		Entry entry = new Entry();
		entry.value = data;
		
		if(hTable[hashValue] == null) {
			hTable[hashValue] = entry;
			return 0;
		}
	}

	public static void main(String[] args) {

	}
}
