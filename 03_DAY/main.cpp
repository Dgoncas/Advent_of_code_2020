#include <bits/stdc++.h>

using namespace std;

int main(){

	vector<string> map;

	string s;
	while(cin>>s){
		map.push_back(s);
	}

	int x=3,y=1;

	int count=0;

	while(y<=map.size()-1){
		if(map[y][x]=='#') count++;
		y+=1;
		x+=3;
		x%= map[0].length();
	}

	cout<<count<<endl;

	return 0;

}