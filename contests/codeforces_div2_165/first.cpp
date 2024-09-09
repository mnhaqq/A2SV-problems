#include <iostream>
#include <vector>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<int> p(n);

    for (int i = 0; i < n; i++) 
    {
        cin >> p[i];
    }

    int changes = 0;
    for (int i = 0; i < n; i++)
    {
        if (p[p[i]-1] == i+1)
        {
            cout << 2 << endl;
            return;
        }
    }
    cout << 3 << endl;

    
}

int main(void)
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        solve();
    }

    return 0;
}