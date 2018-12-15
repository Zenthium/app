#! /usr/bin/env python3
import pyperclip
import pprint
import re

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 1234, ext. 1234, x1234

(((\d\d\d) | (\(\d\d\d\)))?# area code (optional)
(\s | -)# first separator
\d\d\d # first 3 digits
- # separator
\d\d\d\d# last 4 digits
(((ext(\.)?\s) |x)# extension word part (optional)
(\d{2,5}))?) #extension number part (optional)

''', re.VERBOSE)
#Create a regex for email addresses
emailRegex = re.compile('''
[a-zA-Z0-9_+.]+     #name part
@      #@ symbol
[a-zA-Z0-9_+.]+      #domain name part
''', re.VERBOSE)
#Get the text off the clipboard
text = pyperclip.paste()
#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)