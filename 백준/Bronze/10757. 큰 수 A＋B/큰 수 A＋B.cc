#include<iostream>
#include<string>
using namespace std;

int main() {
	string a, b;
	string n = "";
	int s1, s2 = 0;
	int len;

	cin >> a >> b;
	if (a.length() > b.length()) {
		len = a.length();
		while (a.length() != b.length()) {
			b = '0' + b;
		}
	}	
	else {
		len = b.length();
		while (a.length() != b.length()) {
			a = '0' + a;
		}
	}

	for (int i = 1; i <= len; i++) {
		
		s1 = (a[len - i] - '0') + (b[len - i] - '0') + s2;
		if (s1 >= 10) {
			s2 = 1;
			s1 -= 10;
		}
		else
			s2 = 0;

		n = to_string(s1) + n;
		
	}

	if (s2 == 1) {
		n = '1' + n;
	}

	cout << n;
	
	return 0;
}