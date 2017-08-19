from random import randint
l = []
names1 = ['Naman','Jack','Apurv','Abhishek','Shivam','Shreyas','Shashank','Bharath','Piyush','Aakash','Ram','Vedant','Aditya','Ijju','Alekha','Omkar','Rohith','Sudhir','Satyajeet','Smriti','Shivani','Komal','Riya','Arshad','Sudesh','Visham','Vishwajeet','Arpit','Sanket','Atharva','Akshay','Siddhart','Sid','Vedang','Aarti','Pooja','Amit','Indrajeet','Kalindra','Utkarsh','Kesariya','Kesar','Gunny','Sunny','Dolly','Circuit']
names2 = ['Todkar','Gajul','Jain','Verma','Sharma','Agarwal','Kumar','Khan','Mehta','Jagtap','Tadsarkar','Sarda','Dighe','Mane','Mahurkar','Narayan','Teli','Deshpande','Raj','Leone','Bond','Sule','Nalawade','Gandhi','Chiravallai','Selvam','Lalitha','Dongre','Rokhde','Lokhande','Khandare','Kadam','Kokate','Gushi','Mast','Rada','Kale','Gore']
f = open('jack.txt','a')
while(True):
	j = str(randint(100000000000,999999999999))
	j = j[0:4]+" "+j[4:8]+" "+j[8::]
	i = names1[randint(0,len(names1)-1)]
	k = names2[randint(0,len(names2)-1)]
	name = i+" "+k
	if(j not in l):
		l.append(j)
		f.write(j+" "+name+"\n")
print("Done")
