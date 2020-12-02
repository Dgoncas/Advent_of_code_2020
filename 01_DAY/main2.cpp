#include <bits/stdc++.h>

using namespace std;

int main(){

	vector<int> nums;
	bool numb[2021];

	int n;
	while(cin>>n){
		nums.push_back(n);
	}

	for(int i=0;i<nums.size();i++){
		for(int j=i+1;j<nums.size();j++){
			for(int k=j+1;k<nums.size();k++){
				if(nums[i]+nums[j]+nums[k]==2020){
					cout<<nums[i]*nums[j]*nums[k]<<endl;
					return 0;
				}
			}
		}
	}


	return 0;
}