# XML Parsing
import xml.etree.ElementTree as ET

# HTML output

# Interact with user machine
import codecs
import datetime
import re
import sys
from sys import argv
import os
import time
import webbrowser

# Time in milliseconds
second = 1000
minute = second * 60
hour = minute * 60

class Conversation:
	'''base structure to hold SMS conversation info'''
	def __init__(self, party1, party2):
		self.parties = [party1, party2]
		self.messages = []

	def __str__(self):
		returnStr = 'Conversation between ' + party1 + ' and ' + party2
		return returnStr

	def append(self, message):
		self.conversation.append(message)

class SMS:
	'''base SMS class to store a single message'''
	def __init__(self, date, party, message):
		self.date = date
		self.message = message
		self.length = len(message)
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
	conversation = Conversation(party1, party2)
	smsList = conversation.messages
	for sms in root.findall('sms'):
		date = int(sms.attrib['date'])
		if (sms.attrib['type'] == '2'):
			party = party1
		elif (sms.attrib['type'] == '1'):
			party = party2
		# This is to be changed before final release to utf-8 support
		body = str(sms.attrib['body']).encode('ascii', 'ignore')
		newSMS = SMS(date, party, body)
		# Traverse the list backwards,  look for most recent SMS
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

def frequencyChecker(messages):
	'''determine most frequently used words, given an article list to ignore'''
	for message in messages:
		pass

def lengthChecker(messages):
	'''check the lengths of sms messages'''
	lengthDict = {}
	pass

''' For consideration later
def condenseWords(sms):
	# match similar words in an sms with pre-defined list
	removeWords = [wordsList[0], 'a', 'an', 'and', 'the', 'i', 'we', 'us', 'for', 'with', 'am', 'are', 'is', 'he', 'she', 'they', 'have', 'has']
	wordsList = [ 
		['you', 'u'],
		['love', 'luv', 'lub'] ]
'''

def main(party1, party2):
	'''main function that executes program function'''
	parties = [party1, party2]
	messages = transcribe(ET.parse('sms.xml').getroot(), party1, party2)
	frequencies = frequencyChecker(messages)
	lengths = lengthChecker(messages)


if __name__ == '__main__':
	if (len(argv) < 3):
		raise Exception('Please enter your name and then your friend\'s name')
	main(argv[1], argv[2])
