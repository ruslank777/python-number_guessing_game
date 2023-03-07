import os
import random
import smtplib


def send_email():
    user = input("Enter Name >>: ")
    email = input("Enter Email >>: ")
    sender = "gmail address or any other address registered in google"
    message = f"This is a test email for {user}"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # need to replace the first parameter with your email and the second parameter with the google app password
    s.login("gmail address", "<google app pass>")
    s.sendmail(sender, email, message)


if __name__ == '__main__':
    send_email()
