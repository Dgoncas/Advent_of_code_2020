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

		for(auto c3:s){
			if(c3==c) times++;
		}
		if(times>=l1 && times<=l2) ans++;	}

	cout<<ans<<endl;

}