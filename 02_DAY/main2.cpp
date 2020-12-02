#include <bits/stdc++.h>

using namespace std;

int main(){


	int ans=0;
	char c,c2;
	int l1,l2;
	string s;

	while(cin>>l1){
		int times=0;
		cin>>c2>>l2;
		cin>>c;
		cin>>s>>s;

		times+= (s[l1-1]==c) + (s[l2-1]==c);
		if(times==1) ans++;

	}

	cout<<ans<<endl;

}