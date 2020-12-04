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
	bool clear=false;
	int indice=0;

	while(getline(cin,s)){
		indice++;

		for(auto it=fields.begin();it!=fields.end();++it){
			if(s.find(it->first)!= string::npos){
				count++;
				fields[it->first]=true;
			}
		}

		stringstream stream(s);
		string field;

		while(getline(stream,field,' ')){

			if(field.length()<5) continue;
			string data=field.substr(4,field.length());

			if(field.find("byr")!= string::npos){
				if(atoi(data.c_str())<1920 || atoi(data.c_str())>2002){
					clear=true;
				}

			}else if(field.find("iyr")!= string::npos){
				if(atoi(data.c_str())<2010 || atoi(data.c_str())>2020){
					clear=true;
				}

			}else if(field.find("eyr")!= string::npos){
				if(atoi(data.c_str())<2020 || atoi(data.c_str())>2030){
					clear=true;
				}

			}else if(field.find("hgt")!= string::npos){
				if(data.find("cm")!= string::npos){
					data=data.substr(0,data.length()-2);
					if(atoi(data.c_str())<150 || atoi(data.c_str())>193){
						clear=true;
					}
				} else if(data.find("in")!= string::npos){
					data=data.substr(0,data.length()-2);
					if(atoi(data.c_str())<59 || atoi(data.c_str())>76){
						clear=true;					}
				} else{
					clear=true;
				}
				
			}else if(field.find("hcl")!= string::npos){
				if(data[0]!='#'){
					clear=true;
				}
				data=data.substr(1,data.length());
				for(auto c:data){
					if(!(c>='0' && c<='9') && !(c>='a' && c<='f')) clear=true;
				}
			}else if(field.find("ecl")!= string::npos){
				if(data!="amb" && data!="blu" && data!="brn" && data!="gry" && data!="grn" && data!="hzl" && data!="oth"){
					clear=true;
				}
			}else if(field.find("pid")!= string::npos){
				if(data.length()!=9) clear=true;
				for(auto c:data){
					if(c<'0' || c>'9') clear=true;
				}
			}
		}

		if(s.length()==0){
			if((count==8 || (count==7 && !fields["cid"])) && !clear){
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
			clear=false;

			continue;
		}

	}

	cout<<ans<<endl;	

	return 0;

}