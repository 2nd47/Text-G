# XML Parsing
import xml.etree.ElementTree as ET

# HTML output
import dominate as dom
from dominate.tags import *

# Interact with user machine
import datetime
import sys
import os
import time
import webbrowser

SMStree = 0

def transcribe(root):
	'''simplify the extracted SMS XML tree'''
	newTree = ET.Element('smses')
	for sms in root.findall('sms'):
		tempSMS = ET.SubElement(newTree, 'sms')
		if sms.attrib['date_sent'] == 0:
			tempSMS.attrib['party'] = 0
		else:
			tempSMS.attrib['party'] = 1
		tempSMS.attrib['date'] = sms.attrib['date']
		tempSMS.attrib['body'] = sms.attrib['body']
	return root

def main():
	'''main function that executes program function'''
	global SMStree = transcribe(ET.parse('sms.xml'))

if __name__ = 'main':
	main()