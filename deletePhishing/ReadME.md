Author: Michael Matthews
Date: July 14th 2015
Language: Powershell
Reason: This script was written to be an anti-phishing attack script.  In the past we had issues where a phishing attack got past our filters and was sent out to nearly thousands of users.  In order to protect BYU's endusers this script is designed to be sent out immeditately. The script will send the phising email to an Admin account and then the email will be deleted.  

Concerns: What if the search is wrong and deletes valuable emails?
    In order to prevent this we have added a couple of preventitve measures.  First off, we send the email to the admin so it could be recoverd.  Secondly, if there is more than one email that matches the result the email will not be deleted.  Thirdly, if the email does not match the subject exactly (case-sensitive), the sender and the date sent, it will not be deleted.  

For more info go to:

http://thoughtsofanidlemind.com/2014/10/17/using-search-mailbox-to-look-for-items-with-a-specific-date/

http://mikefrobbins.com/2013/12/19/using-powershell-to-remove-phishing-emails-from-user-mailboxes-on-an-exchange-server/

https://technet.microsoft.com/en-us/library/dd298173(v=exchg.150).aspx
