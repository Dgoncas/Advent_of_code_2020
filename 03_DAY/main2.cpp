#include <bits/stdc++.h>

using namespace std;

int main(){

	
	vector<string> map;

	pair<int,int> slopes[5];
	slopes[0]={1,1};
	slopes[1]={3,1};
	slopes[2]={5,1};
	slopes[3]={7,1};
	slopes[4]={1,2};


	long long sol=1;

	for(auto p:slopes){

		string s;
		while(cin>>s){
			map.push_back(s);
		}

		int x=p.first,y=p.second;

		int count=0;

		while(y<=map.size()-1){
			if(map[y][x]=='#') count++;
			y+=p.second;
			x+=p.first;
			x%= map[0].length();
		}

		sol*=count;

	}

	cout<<sol<<endl;

	return 0;

}