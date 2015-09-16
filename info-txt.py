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
 
class ConvParty:
        '''conversation data associated specifically with one participant'''
        def __init__(self, partyName):
                self.name = partyName
                self.data = {}
 
                self.messages = {}
                self.lengths = {}
                self.responseTimes = {}
                self.consecutiveTimes = {}
                self.counts = {}
 
        def _addData(self, data):
                self.data[data.title] = data
 
        def addMessage(self, data):
                pass
 
        def analyze(self):
                self._averages()
                self._medians()
                self._stdevs()
 
class ConvData:
        '''conversation data class for data such as lengths, message body, etc.'''
        def __init__(self, title, parties):
                self.title = title
                # e.g. 'responseTime', 'message', etc.
                self.data = {}
                for party in parties:
                        self.data[party] = []
                self.data['total'] = []
                self.stats = {
                        'average' : [],
                        'median' : [],
                        'stdev' : []
                        'ratio' : []}
 
        def _averages(self, stat):
                return {party: mean(lengths) for party, lengths in stat}
 
        def _medians(self, stat):
                return {party: median_grouped(lengths) for party, lengths in stat}
 
        def _stdevs(self, stat):
                return {party: stdev(lengths) for party, lengths in stat}
 
        def _ratio(self):
                return {party: count / otherCount
                        for party, counts in self.counts
                        for otherParty, otherCounts in self.counts
                        if party != otherParty}
 
        def append(self, party, data):
                self.data[party].append(data)
                self.data['total'].append(data)
 
        def analyze(self):
                for party in self.data:
                        pass
 
class Conversation:
        '''store SMS conversation info'''
        def __init__(self, partyName1, partyName2):
                self.parties = {
                        partyName1 : ConvParty(partyName1),
                        partyName2 : ConvParty(partyName2),
                        'total' : ConvParty('total')}
 
        def __str__(self):
                returnStr = 'Conversation between ' + party1 + ' and ' + party2
                return returnStr
 
        def append(self, message):
                self.parties[message.party].addMessage(message)
                self.parties['total'].addMessage(message)
 
 
                self.messages[message.party].append(message)
                self.messages['total'].append(message)
                self.lengths[message.party].append(message.length)
                self.lengths['total'].append(message)
                self.responseTimes[message.party].append(message.responseTime)
                self.responseTimes['total'].append(message.responseTime)
                self.consecutiveTimes[message.party].append(message.consecutiveTime)
                self.consecutiveTimes['total'].append(message.consecutiveTime)
                self.counts[message.party] += 1
                self.counts['total'] += 1
 
        def analyze(self):
                pass
 
class SMS:
        '''store a single message'''
        def __init__(self, date, party, message):
                self.data = {
                        'date' : date,
                        'message' : message,
                        'length' : len(message),
                        'party' : party,
                        'responseTime' : 0,
                        'consecutiveTime' : 0,
                        'nextMessage' : None
                }
 
        def __getitem__(self, key):
                return self.data[key]
 
        def __setitem__(self, idx, value):
                self.data[idx] = value
 
        def __str__(self):
                returnStr = '[' + str(self.message) + '] '
                returnStr += 'FROM [' + str(self.party) + '] '
                returnStr += 'AT [' + str(self.date) + '] '
                returnStr += 'IN [' + str(self.responseTime) + ']'
                return returnStr
 
def transcribe(root, conversation):
        '''simplify the extracted SMS XML tree'''
        for sms in root.findall('sms'):
                date = int(sms.attrib['date'])
                if (sms.attrib['type'] == '2'):
                        party = conversation.parties[0]
                elif (sms.attrib['type'] == '1'):
                        party = conversation.parties[1]
                ''' Include UTF-8 support when appropriate '''
                body = str(sms.attrib['body']).encode('ascii', 'ignore')
                newSMS = SMS(date, party, body)
                # Traverse the list backwards,  look for most recent SMS
                reversedMessages = reversed(conversation.messages)
                for previousSMS in reversedMessages:
                        if previousSMS[party] == newSMS[party]:
                                if not previousSMS.nextMessage:
                                        previousSMS[nextMessage] = newSMS
                                        newSMS[consecutiveTime] = newSMS[date] - previousSMS[date]
                                break
                        else:
                                newSMS[responseTime] = newSMS[date] - previousSMS[date]
                conversation.append(newSMS)
 
def frequencyChecker(conversation):
        '''determine most frequently used words, given an article list to ignore'''
        pass
 
''' Rework to regex when appropriate
def condenseWords(sms):
        # match similar words in an sms with pre-defined list
        removeWords = [wordsList[0], 'a', 'an', 'and', 'the', 'i', 'we', 'us', 'for', 'with', 'am', 'are', 'is', 'he', 'she', 'they', 'have', 'has']
        wordsList = [
                ['you', 'u'],
                ['love', 'luv', 'lub'] ]
'''
 
def main(party1, party2):
        '''main function that executes program function'''
        convo = Conversation(party1, party2)
        messages = transcribe(ET.parse('sms.xml').getroot(), convo)
 
        convo.analyze()
 
if __name__ == '__main__':
        if (len(argv) < 3):
                raise Exception('Please enter your name and then your contact\'s name')
        main(argv[1], argv[2])