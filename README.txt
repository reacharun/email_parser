“””
@author Arun George
Email parser
“””
The sample parser script parses basic email headers from raw email using regular expressions. 
For the time, it looks at basic structure of header file such as, 'To','From','Subject','Reply-To',
'Content-Type'. Header files compose of a field name, followed by a colon (:), followed by a field body, 
which terminated by a newline. 

Full parsing of email headers can be complex without using a parsing library but the idea itself is not 
very complicated for simple header parsing to maintain readability. For parsing the body part of the email, 
I would look at the MIME messages for the content boundary to figure out the content-type, whether it is 
text/plain, text/html, etc. The email parts can be split into 3 sections: the message content 
(which may be in plain text or HTML), data related to the message such as the logo (usually in HTML), 
and attachments, which you can save as separate files.

The before and after screen shot of this simple parsing can be seen here:
http://mylab.algoy.com/screen.jpg
