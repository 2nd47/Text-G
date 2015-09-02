# XML Parsing
import xml.etree.ElementTree as ET

# HTML output
import dominate as dom
from dominate.tags import *

# Interact with user machine
import datetime
from sys import argv
import os
import time
import webbrowser

second = 1000
minute = 60000
hour = 3600000

class SMS:
	'''base SMS class to store a single message'''
	def __init__(self, date, party, message):
		self.date = date
		self.message = message
		self.party = party
		self.responseTime = 0

def transcribe(root, party1, party2):
	'''simplify the extracted SMS XML tree'''
	SMSlist = []
	for sms in root.findall('sms'):
		newSMS = SMS(sms.attrib['date'], sms.attrib['type'], sms.attrib['body'])
		SMSlist.append(newSMS)
	return SMSlist

def main(party1, party2):
	'''main function that executes program function'''
	messages = transcribe(ET.parse('sms.xml').getroot(), party1, party2)

if __name__ == '__main__':
	if (len(argv) < 3):
		raise Exception('Please enter your name and then your friend\'s name')
	main(argv[1], argv[2])
