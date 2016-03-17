Database Status
===============
This script verifies that the databases 13DB1-13DB30 are "healthy".  If they aren't it sends out an email to the lead engineer notifying him of the issue.  The results of the script are logged daily on CA6 under `D:\Reports\DatabaseStatus\DatabaseStatus.txt`


Possible Problems
==========
If the script reports a false-positive this most likely would be due to the fact that the script assumes that the first 30 DB returned from Get-MailboxDatabase are the relevant DB.  If more DB's are added or if the order is switched the script will need to be modified to take this into account. 

Common Questions
=========

What can they consume in Nagios from this script?

Nagios currently monitors the status of the mailbox database. If there is a mailbox that is not "healthy" then Nagios will report this as "critical".  Also an email will be sent to all those who are in the email list.  

What other status does (other than healthy) does this command give?

The possible status of the mailbox databases are: healthy, crawling, unknown, failed, disabled, and FailedAndSuspended

Where is this information logged?

Everytime this script runs, the data is logged on CA6 under `D:\Reports\DatabaseStatusEmail`

Where is the diagram?

The diagram can be found on the sharepoint website. Further Documentaiton can also be found there

`https://ese.byu.edu/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2FShared%20Documents%2FEMAIL%2FMailboxDatabaseStatus&FolderCTID=0x0120008D0685836200314B81DE9145B0239B34&View=%7BB3110036-F203-4EFF-8A2F-3CB64A50D17A%7D` 


Get Help
========

Get-MailboxDatabaseCopyStatus

`https://technet.microsoft.com/en-us/library/dd298044%28v=exchg.150%29.aspx`