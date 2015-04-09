from apscheduler.scheduler import Scheduler
import requests
import difflib
import subprocess as sp
import sched, time
import threading
import time
sp.call("notify-send"+" WAIT"+" Result\ will\ be\ checked\ in\ 60\ seconds",shell= True)
timeout = 1
def checkResult():
	r  = requests.get('http://www.uptu.ac.in/results/mtu_result_14_15.htm')
	f = open("result.html",'r')
	original = f.read()
	a = ''
	text = ''
	# print "THE VALUE OF A IS"
	with open('result.html', 'r') as content_file:
		a = a+str(content_file.read())
	d = difflib.Differ()
	diff = d.compare(a,r.text)
	text = text.join(diff)
	text = text.replace(' ','')
	text = text.replace('\n','')
	if text.find('B.Tech.FifthSemesterResult2014-15') != -1:
		sp.call("notify-send"+" Uptu-Result"+" 5th\ Semester\ Result\ is\ Out\ -t\ 300000",shell=True)
	else:
		sp.call("notify-send"+" Uptu-Result"+" Sorry\ Result\ Not\ Updated",shell= True)
	f.close()
	sp.call("notify-send"+" WAIT"+" Result\ will\ be\ checked\ again\ in\ 60\ seconds",shell= True)
while True:
	if time.time() > timeout:
		checkResult()
		timeout = time.time() + 60
