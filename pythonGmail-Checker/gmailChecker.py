#!/usr/bin/env python
#for some reason future needs to be at the top
#this import changes the way the the print command works

from __future__ import print_function

_author_ = "Michael Matthews"
"""

Sending Email
Date: Oct. 7th 2015

This script is designed to log into a gmail account and send an email
to a @byu.edu address. The @byu.edu address is set up to automatically bounce the message
to a seperate gmail account. The script then logs into the second gmail account
and verifies that the same email that was sent arrived.

If the same email that was sent arrives, the the time sent, time receieved and the IP address
are all logged. Else, the time sent (since we don't have a receive time) is logged in the errors.txt file


"""

#this should be 600 seconds for a ten minute run
#the script will send the email and then wait to check for the number of seconds below
wait = 600


#importing necessary libraries
import smtplib, imaplib, email, time, re, json
from datetime import datetime
file_path = open('config.py', 'r')
json_file = file_path.read()
json_data = json.loads(json_file)


#setting start time
start = time.time()

#Sending the message
fromaddr = json_data["credentials"][0]["username2"]
toaddr = 'postmaster@byu.edu'
msg = 'Subject: %s\n\n%s' % (start, 'This email is sent in order to verify if BYU mail flow is working correctly')


#Credentials
username = json_data["credentials"][0]["username2"]
password = json_data["credentials"][0]["password"]

#The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
sent_time = datetime.now()
server.sendmail(fromaddr, toaddr, msg)
server.quit()

#Having the script wait so that the email can get there
time.sleep(wait)

#Opening up GMAIL account
def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login(json_data["credentials"][0]["username"], json_data["credentials"][0]["password"])
conn.select()
typ, data = conn.search(None, 'UNSEEN')
subject = "1232112312"
subject_ID = "FW: " + str(start)

#I set the "subject" above to a random number so that is isnt' undefined
#if the subject doesn't match what was sent out then it'll report an error

try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])

                subject = msg['subject']
                received = msg['Received']
                received_ip = received[0:16]
                match_time = re.findall(r'[a-zA-Z]{3}\W\s\d*\s[a-zA-Z]{3}\s\d{4}\s\d{2}\W\d{2}\W\d{2}', received)

                #for some reason I needed to import this libraries further along the script because I was importing
                #datetime differently for different reasons

                import pytz
                from datetime import timedelta
                import datetime


                local = pytz.timezone ("America/Los_Angeles")

                #match_time is a list, so you need to find the first element of that list
               	naive = datetime.datetime.strptime (match_time[0], "%a, %d %b %Y %H:%M:%S")

                #The subject on the message will have "FW: " at the beginning plus the start time.
                #This is used to define if it is the same email that was sent. Keep in mind that the sent
                #time is the subject and so therefore is unique

                subject_ID = "FW: " + str(start)

                payload=msg.get_payload()
                body=extract_body(payload)


        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()

#This subtracts the send date and return date
###Converting string to float
counter = 0
errorCounter = 0
while counter == 0:

        parseSubject = subject[4:]
        subjectFloat = int(float(parseSubject))
        done = time.time()
        #elapsed = done - subjectFloat

        #This conditional statement is if the subject of the returned email matches the one that was sent
        if subject == subject_ID:

            new = naive + timedelta(hours=1)

            log = open("results.txt", "a")
            print(received_ip, "!", file = log)
            print(sent_time.strftime("%H:%M:%S %m-%d"), "!", file = log)
            print(new.strftime("%H:%M:%S %m-%d"), "!", file = log)

            #counter
            counter = 1

        else:

            errorCounter = errorCounter + 1

            if errorCounter > 2:

                counter = 1

            if errorCounter == 1:

                log = open("errors.txt", "a")
                print(sent_time.strftime("%H:%M:%S %m-%d"), "!", file = log)

            #This is the email that the error message will be sent to
            toaddrError = json_data["results"][0]["send_to"]
            msgError = 'Subject: %s\n\n%s' % (start, 'There was an error in sending the script')

            #Sending the message
            fromaddr = json_data["credentials"][0]["username2"]

            #Credentials
            username = json_data["credentials"][0]["username2"]
            password = json_data["credentials"][0]["password"]

            #The actual mail send
            server = smtplib.SMTP('smtp.gmail.com:587')

            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrError, msgError)
            server.quit()
