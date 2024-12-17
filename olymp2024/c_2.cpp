#include <iostream>

int main() {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    if (B == C) {
        cout << A + D + B + C;
    } else if (!B  && !C) {
        cout << max(A, D);
    } else {
        cout << A + D + min(B,C) * 2 + 1;
    }
}