import csv
batsman=open("output2.txt")#batsman
bowler=open("output2_bowler.txt")#bowler
a=bowler.read().split("\n");
c = batsman.read().split("\n");
b=open("stadium.csv").read().split("\n");

d={}
n={}
m=[]
o={}
rw={} 
for i in b:
	x=i.split(",")
	if(len(x)==2):
		x[0]=x[0].strip()
		x[0]=x[0].strip("'");
		x[0]=x[0].strip('"')
		if x[0] not in d:
			d[x[0]]=float(x[1])



for i in c:
	x=(i.split(","));	
	if(len(x)==12):	
		x[0]=x[0].replace("_"," ");
		if x[0] not in o:
			o[x[0]]=[]
		o[x[0]].append(float(x[11]));
	

for i in a:
	x=(i.split(","));	
	if(len(x)==14):	
		x[0]=x[0].replace("_"," ");
		if x[0] not in n:
			n[x[0]]=[]
		n[x[0]].append(float(x[13]));

for i in a:
	x=(i.split(","));	
	if(len(x)==14):	
		x[0]=x[0].replace("_"," ");
		if x[0] not in rw:
			rw[x[0]]=[]
		rw[x[0]].append(float(x[12]));




bat1=input("Enter the name of the first Batsman ");
bat2=input("Enter the name of the Second Batsman ")
bowl1=input("Enter the name of the first Bowler ")
bowl2=input("Enter the name of the second Bowler ")
bowl3=input("Enter the name of the third Bowler ")
bowl4=input("Enter the name of the fourth Bowler ")
O_no=input("Enter the over set number : ")
stad=input("Enter the name of the stadium : ")

br1=o[bat1][int(O_no)-1]
br2=o[bat1][int(O_no)-1]
bo1=n[bowl1][int(O_no)-1]
bo2=n[bowl2][int(O_no)-1]
bo3=n[bowl3][int(O_no)-1]
bo4=n[bowl4][int(O_no)-1]

borw1=rw[bowl1][int(O_no)-1]
borw2=rw[bowl2][int(O_no)-1]
borw3=rw[bowl3][int(O_no)-1]
borw4=rw[bowl4][int(O_no)-1]
st=d[stad]
print(br1,br2,bo1,bo2,bo3,bo4,borw1,borw2,borw3,borw4,st)

avgrw = (borw1+borw2+borw3+borw4)/4.0













