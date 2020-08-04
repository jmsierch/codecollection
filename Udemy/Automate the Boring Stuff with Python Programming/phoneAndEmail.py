#! python 3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext., x12345
(
((\d\d\d) | (\(\d\d\d\)))?    # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
((ext(\.)?\s |x)            # extension word-part
(\d{2,5}))?                # extension
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com
([a-zA-Z0-9_.+]+       #name part
@                      #@ symbol
[a-zA-Z0-9_.+]+        #domain name part
(\.[a-zA-Z]{2,4}))     #.com section
''',re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allEmailAddresses = []
for emailAddress in extractedEmail:
    allEmailAddresses.append(emailAddress[0])

# Copy the extract email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmailAddresses)
pyperclip.copy(results)
