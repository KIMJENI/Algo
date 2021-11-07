#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	deque<int> deq;
	int x, n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> s;
		if (s == "push_front") {
			cin >> x;
			deq.push_front(x);
		}
		else if (s == "push_back") {
			cin >> x;
			deq.push_back(x);
		}
		else if (s == "pop_front") {
			if (!deq.empty()) {
				cout << deq.front() << '\n';
				deq.pop_front();
			}
			else cout << "-1" << '\n';
		}
		else if (s == "pop_back") {
			if (!deq.empty()) {
				cout << deq.back() << '\n';
				deq.pop_back();
			}
			else cout << "-1" << '\n';
		}
		else if (s == "size") cout << deq.size() << '\n';
		else if (s == "empty") {
			if (deq.empty()) cout << "1" << '\n';
			else cout << "0" << '\n';
		}
		else if (s == "front") {
			if (!deq.empty()) {
				cout << deq.front() << '\n';
			}
			else cout << "-1" << '\n';
		}
		else if (s == "back") {
			if (!deq.empty()) {
				cout << deq.back() << '\n';
			}
			else cout << "-1" << '\n';
		}
	}
	return 0;
}