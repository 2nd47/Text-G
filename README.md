Introduction
==========

This is a simple Python app written to take exported text messages and output some cool facts about a conversations you've been having such as:

* Most frequently used words [by party]
* Response time (average, median) [by party]
* Count of "I love you" messages and their alternatives in time chunks [by party]
* Count of swearing [by party]
* Average length of SMS message [by party]

Requirements
----------

* An Android phone with the "SMS Backup & Restore" app which is available for free on the Play Store. 

How to use
----------

* Backup a single conversation without MMS. Retrieve the saved *.xml file from your phone and place it in the same directory as the program, making sure to rename it as "sms.xml".