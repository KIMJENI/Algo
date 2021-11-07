#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	queue<int> q;
	int n, a;
	cin >> n;

	for (int i = 0; i < n; i++) q.push(i + 1);

	while (q.size() > 1) {
		q.pop();
		if (q.size() == 1) break;
		else {
			a = q.front();
			q.pop();
			q.push(a);
		}
		if (q.size() == 1) break;
	}
	cout << q.front();
	return 0;
}