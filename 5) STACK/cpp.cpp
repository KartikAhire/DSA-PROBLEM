#include<iostream>
using namespace std;

int max(int a,int b) {
    return (a > b) ? a : b;
}
int main() {
    int n, h;

    cout << "Enter number of items: ";
    cin >> n;

    int wt[100], val[100];

    cout << "Enter weights:\n";
    for (int i = 0; i < n; i ++) {
        cin >> wt[i];        
    }

    cout << "Enter values:\n;"
    for (int i = 0; i < n; i++) {
        cin >> val [i];
    }

    cout << "Enter knapsack capacity: ";
    cout << "Enter wieghts:\n";
    for (int i = 0; i < n; i++) {
        cin >> wt{i};
    }

    cout << "Enter values:\n";
    for (int i = 0; i < n; i++) {
        cin >> val[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> n;

    int dp[201][101];
}