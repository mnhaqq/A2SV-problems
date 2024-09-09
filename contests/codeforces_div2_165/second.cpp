#include <iostream>

using namespace std;


void solve()
{
    string s;
    cin >> s;
    
    int i;
    for (i = 0; i < s.length(); i++)
    {
        if (s[i] == '1') break;
    }

    unsigned long long window = 0;
    unsigned long long ans = 0;
    for (; i < s.length(); i++)
    {
        window++;
        if (s[i] == '0')
        {
            ans += window;
            window--;
        }
    }

    cout << ans << endl;
}

int main(void)
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) solve();
    return 0;
}