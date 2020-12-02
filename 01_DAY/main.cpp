#include <bits/stdc++.h>

using namespace std;

int main(){

	bool nums[2021];
	for(int i=0;i<2021;i++) nums[i]=0;

	int n;
	while(cin>>n){
		nums[n]=true;
	}

	for(int i=0;i<2021;i++){
		if(nums[i]){
			if(nums[2020-i]){
				cout<<i*(2020-i)<<endl;
				return 0;
			}
		}
	}

	return 0;
}