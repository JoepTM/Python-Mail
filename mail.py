import getpass
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print ("""
 /##      /##           /## /##
| ###    /###          |__/| ##
| ####  /####  /######  /##| ##
| ## ##/## ## |____  ##| ##| ##
| ##  ###| ##  /#######| ##| ##
| ##\  # | ## /##__  ##| ##| ##
| ## \/  | ##|  #######| ##| ##
|__/     |__/ \_______/|__/|__/
""")

sender_email = "your-mail@gmail.com"
receiver_email = "receiver-mail@gmail.com"
password = getpass.getpass("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
HI,
This is a test mail send with python.
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       This is a test mail send with python.<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
except smtplib.SMTPAuthenticationError:
    print ("""\n
 /#### /## /####  /######                                         
| ##_/| ##|_  ## /##__  ##                                        
| ##  | ##  | ##| ##  \ ##  /#######  /#######  /######   /#######
| ##  | ##  | ##| ######## /##_____/ /##_____/ /##__  ## /##_____/
| ##  |__/  | ##| ##__  ##| ##      | ##      | ########|  ###### 
| ##        | ##| ##  | ##| ##      | ##      | ##_____/ \____  ##
| #### /## /####| ##  | ##|  #######|  #######|  ####### /#######/
|____/|__/|____/|__/  |__/ \_______/ \_______/ \_______/|_______/  
Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps
            """)
