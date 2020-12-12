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

sender_email = "bobusessocks@gmail.com"
receiver_email = "joepvermue@gmail.com"
password = getpass.getpass("Type your password and press enter: ")
subject = input("Type the subject of the mail: ")

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

def typeText():
    print("Type the mail you want to send: ")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    mailText = '\n'.join(lines)
       
    if len(mailText) == 0:
        print("You cant leave the message blank.")
        typeText()
    else:
        print(mailText)
        yn = input("\nThis is your mail  right now, do you want to send it like this? y/n: ")

        if yn == "y":

            try:
                # Attach the typed stuff to the mail.
                part1 = MIMEText(mailText, "plain")
                message.attach(part1)
                # Create secure connection with server and send email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
                print("""
  /$$$$$$                                                             
 /$$__  $$                                                            
| $$  \__/ /$$   /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$$
|  $$$$$$ | $$  | $$ /$$_____/ /$$_____/ /$$__  $$ /$$_____/ /$$_____/
 \____  $$| $$  | $$| $$      | $$      | $$$$$$$$|  $$$$$$ |  $$$$$$ 
 /$$  \ $$| $$  | $$| $$      | $$      | $$_____/ \____  $$ \____  $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/ /$$$$$$$/
 \______/  \______/  \_______/ \_______/ \_______/|_______/ |_______/
Succesfully send the E-Mail to""", receiver_email)
            except smtplib.SMTPAuthenticationError:
                print("""
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
        elif yn == "n":
            typeText()
typeText()
