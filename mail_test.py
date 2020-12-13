import getpass
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

os.system("cls") #use this for windows. change to os.system("clear") for linux

COLORS = {
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
}

acces = open(".//ascii//acces.txt","r")
succes = open(".//ascii//succes.txt","r")
error = open(".//ascii//error.txt","r")
logo = open(".//ascii//logo.txt","r")

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

ascii = "".join(logo.readlines())
print(colorText(ascii))

def main():
        sender_email = input("Type your E-Mail: ")
        password = getpass.getpass("Type your password and press enter: ")
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.quit()
            receiver_email = input("Type the resiver their E-Mail: ")
            subject = input("Type the subject of the mail: ")
            
            def typeText():
                message = MIMEMultipart("alternative")
                message["Subject"] = subject
                message["From"] = sender_email
                message["To"] = receiver_email
                
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
                            part1 = MIMEText(mailText, "plain")
                            message.attach(part1)
                            context = ssl.create_default_context()
                            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login(sender_email, password)
                                server.sendmail(
                                    sender_email, receiver_email, message.as_string()
                                )
                            ascii = "".join(succes.readlines())
                            print(colorText(succes))
                        except smtplib.SMTPAuthenticationError:
                            ascii = "".join(acces.readlines())
                            print(colorText(ascii))
                            print(a)
                            os.system("pause")
                        except Exception as a:
                            ascii = "".join(error.readlines())
                            print(colorText(ascii))
                            print(a)
                            os.system("pause")
                    else:
                        typeText()
            typeText()
                            
        except smtplib.SMTPAuthenticationError:
            ascii = "".join(acces.readlines())
            print(colorText(ascii))
main()
