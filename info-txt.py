# XML Parsing
import xml.etree.ElementTree as ET

# NLP data analysis
import nltk
nltk.download()
from nltk.corpus import stopwords

# Interact with user machine
from enum import Enum
import re
import sys
from sys import argv
import os

# INCLUDE HOW MANY WISHES WERE MADE
# INCLUDE LONGEST STREAK OF TEXT MESSAGES

# Time In Milliseconds
class TIM(Enum):
	''' Time in milliseconds'''
	SECOND = 1000,
	MINUTE = SECOND * 60,
	HOUR = MINUTE * 60,
	DAY = HOUR * 24,
	WEEK = DAY * 7,
	# 30d/mo; 365d/yr
	MONTH = WEEK * 4 + DAY * 2,
	YEAR = MONTH * 12 + DAY * 5,

class NLPAnalyze:
	# REWORK IMMEDIATELY
	# REWORK IMMEDIATELY
	# REWORK IMMEDIATELY
	'''all NLP analysis starts here'''
	def __init__(self):
		# Some basic regex
		self.laugh = re.compile('[h[e|a]]{2,}')
		self.love = re.compile('[l+[u|o]+v+e*]')
		self.you = re.compile('[[y+o+u+]|u+]')
		self.swear = re.compile('[f+[a|u]+[c|k]+] | [s+h+i+t+] | [c+u+n+t+]')
		self.babey = re.compile('[b+a+b+[e+|y+]]')
		self.heart = re.compile('<+3+')

		# Remove stop words
		cachedStopWords = stopwords.words('english')
		[word for word in text if word not in cachedStopWords]
		# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
		# Really cool feature to examine changes through time


class ConvParty:
	"""Store data for a conversation participant and their associated data
	"""
	def __init__(self, partyName):
		self.name = partyName
		self.dataSet = {
			'sms' : ConvData('sms'),
			'length' : ConvData('length'),
			'responseTime' : ConvData('responseTime'),
			'timeToNext' : ConvData('timeToNext')
		}

	def __getitem__(self, key):
		'''index over the dataSet'''
		if key == 'name':
				return self.name
		if key in self.data:
			return self.dataSet[key]
				return None

	def __setitem__(self, idx, value):
		'''index over the dataSet'''
		if key in self.data:
			self.dataSet[idx] = value

	def __str__(self):
		returnStr = 'DATA FOR ' + self.name
		return returnStr

	def addSMS(self, sms):
		self['sms'] += sms
		self['length'] += sms['length']
		if sms['responseTime'] > 0:
				self['responseTime'] += sms['responseTime']
		if sms['timeToNext'] > 0:
				self['timeToNext'] += sms['timeToNext']

	def analyze(self):
		print('Analyzing data for ' + self.name + '...')
		for data in self.dataSet:
				data.analyze()
		# Do NLTK analysis here


class ConvData:
	"""Store conversation data associated with one particpant and one data type
	"""
	def __init__(self, title):
	# e.g. 'responseTime', 'message', 'length', etc.
	self.title = title
	self.data = []
	self.count = 0
	self.stats = {}

	def __add__(self, other):
		self.data += other
		self.count += 1
		return self

	def __iadd__(self, other):
		self.data += other
		self.count += 1
		return self

	def __str__(self):
		returnStr = self.title + ' WITH ' + self.count
		return returnStr

	def analyze(self, other=None):
		if not self.stats:
			self.stats['average'] = mean(self.data)
			self.stats['median'] = median_grouped(self.data)
			self.stats['mode'] = mode(self.data)
			self.stats['stdev'] = stdev(self.data)


class Conversation:
	"""Store data for a conversation given two participants.
		This will also store values for both participants combined
		"""
	def __init__(self, party1, party2):
		self.parties = {
			'party1' : ConvParty(partyName1),
			'party2' : ConvParty(partyName2),
			'total' : ConvParty('total')}

	def __getitem__(self, key):
		if key in self.parties:
			return self.parties[key]
		return None

	def __str__(self):
		returnStr = 'Conversation between ' + party1 + ' and ' + party2
		return returnStr

	def addSMS(self, sms):
		self[sms[party]].addSMS(sms)
		self['total'].addSMS(sms)

	def analyze(self):
		for party in self.parties:
			party.analyze()


class SMS:
	"""Store data for a single SMS
		"""
	def __init__(self, date, party, message):
		self.data = {
			'date' : date,
			'message' : message,
			'length' : len(message),
			'party' : party,
			'responseTime' : 0,
			'timeToNext' : 0,
						'wish' : False
		}
		self._checkWish()

	def __getitem__(self, key):
		if key in self.data:
			return self.data[key]
		return None

	def __setitem__(self, idx, value):
		self.data[idx] = value

	def __str__(self):
		returnStr = '[' + str(self.message) + '] '
		returnStr += 'FROM [' + str(self.party) + '] '
		returnStr += 'AT [' + str(self.date) + '] '
		returnStr += 'IN [' + str(self.responseTime) + ']'
		return returnStr

	def _checkWish():
		'''check if a wish was made around 11:11/23:11 with this SMS'''
        pass


def transcribe(root, conversation):
	"""Parse ElementTree XML and fill conversation object with relevant data
	"""
	print('Parsing messages from XML file...')
	for sms in root.findall('sms'):
		# Input time as milliseconds
		date = int(sms.attrib['date'])
		# Determine which party sent the message
		if (sms.attrib['type'] == '2'):
			party = conversation['party1']['name']
		elif (sms.attrib['type'] == '1'):
			party = conversation['party2']['name']
		# Include UTF-8 and Emoji support in later revisions
		message = str(sms.attrib['body']).encode('ascii', 'ignore')
		newSMS = SMS(date, party, message)
		# Traverse the list backwards, get most recent SMS from both parties
		reversedSMSs = reversed(conversation.messages)
		for previousSMS in reversedSMSs:
			if previousSMS[party] == newSMS[party]:
				# Set the time between responses for one party
				if not previousSMS[timeToNext]:
					previousSMS[timeToNext] = newSMS[date] - previousSMS[date]
				else:
					break
					# Set the time it took to respond to the other party
    		else:
				newSMS[responseTime] = newSMS[date] - previousSMS[date]
		conversation.addSMS(newSMS)
		print('Successfully parsed ' + conversation['total']['sms'].count + ' messages!')

def main(party1, party2):
	'''main function that executes program function'''
	# Initialize conversation participants
	partyData1 = ConvParty(party1)
	partyData2 = ConvParty(party2)
	# Initialize conversation
	convo = Conversation(party1, party2)
	# Parse messages into conversation from ET-parsed XML file
	messages = transcribe(ET.parse('sms.xml').getroot(), convo)
	# Perform analysis on the gathered SMS data
	convo.analyze()
	# Initialize graphics output

if __name__ == '__main__':
	if (len(argv) < 3):
		raise Exception('Please enter your name and then your contact\'s name')
	main(argv[1], argv[2])
