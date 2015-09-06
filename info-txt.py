# XML Parsing
import xml.etree.ElementTree as ET

# HTML output

# Interact with user machine
import codecs
import datetime
import sys
from sys import argv
import os
import time
import webbrowser

# Time in milliseconds
second = 1000
minute = 60000
hour = 3600000

class SMS:
	'''base SMS class to store a single message'''
	def __init__(self, date=0, party='0', message='0'):
		self.date = date
		self.message = message
		self.party = party
		self.responseTime = 0

	def __str__(self):
		returnStr = '[' + str(self.message) + '] '
		returnStr += 'FROM [' + str(self.party) + '] '
		returnStr += 'AT [' + str(self.date) + '] '
		returnStr += 'IN [' + str(self.responseTime) + ']'
		return returnStr

def transcribe(root, party1, party2):
	'''simplify the extracted SMS XML tree'''
	smsList = []
	for sms in root.findall('sms'):
		date = int(sms.attrib['date'])
		if (sms.attrib['type'] == '2'):
			party = party1
		elif (sms.attrib['type'] == '1'):
			party = party2
		# This is to be changed before final release to utf-8 support
		body = str(sms.attrib['body']).encode('ascii', 'ignore')
		newSMS = SMS(date, party, body)
		# Traverse the list backwards, skip the new entry we added
		reversedMessages = reversed(smsList)
		for sms in smsList:
			print(sms)
		input('test:')
		for previousSMS in reversedMessages:
			if previousSMS.party == newSMS.party:
				break
			else:
				newSMS.responseTime = newSMS.date - previousSMS.date
		smsList.append(newSMS)
	return smsList

def main(party1, party2):
	'''main function that executes program function'''
	messages = transcribe(ET.parse('sms.xml').getroot(), party1, party2)

if __name__ == '__main__':
	if (len(argv) < 3):
		raise Exception('Please enter your name and then your friend\'s name')
	main(argv[1], argv[2])
