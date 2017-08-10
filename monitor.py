#!/usr/bin/python
import sys, getopt, time
import requests
import Adafruit_CharLCD as LCD

reload(sys)
sys.setdefaultencoding('latin1')

class RBL:
	id = 0
	line = ''
	station = ''
	direction = ''
	time = -1

def replaceUmlaut(s):
	s = s.replace(chr(196), "Ae") # A umlaut
	s = s.replace(chr(214), "Oe") # O umlaut
	s = s.replace(chr(220), "Ue") # U umlaut
	s = s.replace(chr(228), "ae") # a umlaut
	s = s.replace(chr(223), "ss") # Sharp s
	s = s.replace(chr(246), "oe") # o umlaut
	s = s.replace(chr(252), "ue") # u umlaut
	return s

def main(argv):
	
	apikey = False
	apiurl = 'https://www.wienerlinien.at/ogd_realtime/monitor?rbl={rbl}&sender={apikey}'
	st = 10

	try:                                
		opts, args = getopt.getopt(argv, "hk:t:", ["help", "key=", "time="])
	except getopt.GetoptError:          
		usage()                         
		sys.exit(2)                     
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()                     
			sys.exit()                                    
		elif opt in ("-k", "--key"):
			apikey = arg
		elif opt in ("-t", "--time"):
			try:
				tmpst = int(arg)
				if tmpst > 0:
					st = tmpst
			except ValueError:
				usage()
                		sys.exit(2)


	if apikey == False or len(args) < 1:
		usage()
		sys.exit()
	
	rbls = []
	for rbl in args:
		tmprbl = RBL()
		tmprbl.id = rbl
		rbls.append(tmprbl)
	
	global lcd 
	lcd = lcd = LCD.Adafruit_CharLCDPlate()
	lcd.clear()
	
	x = 1	
	while True:
		for rbl in rbls:
			url = apiurl.replace('{apikey}', apikey).replace('{rbl}', rbl.id)
			r = requests.get(url)
			if r.status_code == 200:
				try:
					for monitor in r.json()['data']['monitors']:
						rbl.station = monitor['locationStop']['properties']['title']
						for line in monitor['lines']:
							rbl.line = line['name']
							rbl.direction = line['towards']
							rbl.time = line['departures']['departure'][0]['departureTime']['countdown']
							#dumpRBL(rbl)
							lcdShow(rbl)
							time.sleep(st)
				except:
					print "some error occurred try next one ..."

def lcdShow(rbl):
	lcd.clear()
	lcd.message(replaceUmlaut(rbl.line + ' ' + rbl.station + '\n' + '{:0>2d}'.format(rbl.time) + ' ' + rbl.direction))

def dumpRBL(rbl):
	print rbl.line + ' ' + rbl.station
	print rbl.direction
	print str(rbl.time) + ' Min.'
	
def usage():
	print 'usage: ' + __file__ + ' [-h] [-t time] -k apikey rbl [rbl ...]\n';
	print 'arguments:'
	print '  -k, --key=\tAPI key'
	print '  rbl\t\tRBL number\n'
	print 'optional arguments:'
	print '  -h, --help\tshow this help'
	print '  -t, --time=\ttime between station updates in seconds, default 10'

if __name__ == "__main__":
	main(sys.argv[1:])
