# XML Parsing
import xml.etree.ElementTree as ET

# Interact with user machine
from enum import Enum
import re
import sys
from sys import argv
import os

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

def transcribe(root, conversation):
	'''simplify the extracted SMS XML tree'''
	smsList = conversation.messages
	for sms in root.findall('sms'):
		date = int(sms.attrib['date'])
		if (sms.attrib['type'] == '2'):
			party = conversation.parties[0]
		elif (sms.attrib['type'] == '1'):
			party = conversation.parties[1]
		# This is to be changed before final release to utf-8 support
		body = str(sms.attrib['body']).encode('ascii', 'ignore')
		newSMS = SMS(date, party, body)
		# Traverse the list backwards,  look for most recent SMS
		reversedMessages = reversed(smsList)
		for previousSMS in reversedMessages:
			if previousSMS.party == newSMS.party:
				break
			else:
				newSMS.responseTime = newSMS.date - previousSMS.date
		smsList.append(newSMS)

def frequencyChecker(conversation):
	'''determine most frequently used words, given an article list to ignore'''
	for message in conversation.messages:
		pass

def lengthChecker(conversation):
	'''check the lengths of sms messages'''
	messageLengths = {}
	messageCount = {}
	for party in conversation.parties:
		messageLengths[party] = []
		for message in conversation.messages:
			if party == message.party:
				messageLengths[party].append(message.length)
		messageCount[party] = len(messageLengths[party])

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
	conversation = Conversation(party1, party2)
	messages = transcribe(ET.parse('sms.xml').getroot(), conversation)
	frequencies = frequencyChecker(conversation)
	lengths = lengthChecker(conversation)


if __name__ == '__main__':
	if (len(argv) < 3):
		raise Exception('Please enter your name and then your friend\'s name')
	main(argv[1], argv[2])
