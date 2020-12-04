#include <bits/stdc++.h>

using namespace std;

int main(){


	map<string,bool> fields;

	fields["byr"]=false;
	fields["iyr"]=false;
	fields["eyr"]=false;
	fields["hgt"]=false;
	fields["hcl"]=false;
	fields["ecl"]=false;
	fields["pid"]=false;
	fields["cid"]=false;


	string s;

	int count=0;
	int ans=0;

	while(getline(cin,s)){


		for(auto it=fields.begin();it!=fields.end();++it){
			if(s.find(it->first)!= string::npos){
				count++;
				fields[it->first]=true;
			}
		}

		if(s.length()==0){
			if(count==8 || (count==7 && !fields["cid"])){
				ans++;
			}

			count=0;
			fields["byr"]=false;
			fields["iyr"]=false;
			fields["eyr"]=false;
			fields["hgt"]=false;
			fields["hcl"]=false;
			fields["ecl"]=false;
			fields["pid"]=false;
			fields["cid"]=false;

			continue;
		}

	}

	cout<<ans<<endl;	

	return 0;

}