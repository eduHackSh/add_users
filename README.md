# add_users
A Python program that add users in Linux system using a structured document and send personalized email for them.

Installation:
 - Clone the repository in your system:
  $ git clone https://github.com/eduHackSh/add_users.git
 - Install the requeriments that not are installed in your system:
  $ python3 -m pip install dotenv
  Note: if you don't want to send mail to the users, change the confirmMail variable to False in main.py file.

Use guide:
  1) Edit the .env file to change MAIL_PASSWORD and MAIL_ADDRESS. These are YOUR credentials to send mail and login with smtp server.
  2) Edit the body.txt file:
    - The first pair of keys "ASUNTO:{any subject}" contain the subject of the email.
    - The second pair of keys "CUERPO:{any body}" contain the body of the email.
    - Inside the file exists variables what can you use to make the email personalized to the user.
      $USER (user id), $PASSWORD (user password), $NAME and $SURNAME (name and surname of the user).
      You can use this variables anywhere in the message and the program change this part to the data of current user.
  3) You must decide what type of file to use, and put in the program directory:
    - If you have a excel (.xlsx):
      The excel sheet has to be structured as follow:
      [![archivo-de-ejemplo-excel-edit.jpg](https://i.postimg.cc/rmM0scfw/archivo-de-ejemplo-excel-edit.jpg)](https://postimg.cc/1g75Yxxk)
    - If you have a txt (strictly named "lista.txt"):
      The text has to be structured as follow:
      [![archivo-de-ejemplo-txt-edit.jpg](https://i.postimg.cc/J024mWy0/archivo-de-ejemplo-txt-edit.jpg)](https://postimg.cc/dZGKmpjc)
  4) Excecute main.py as sudo (or changes the permissions for add users) and follow the instructions it will give you.

Files:
  - .env -> Have the credentials of the email sender. Note: MAIL_PASSWORD is not your email password. Check: https://hotter.io/docs/email-accounts/app-password-gmail/
  - body.py -> Contain the get_message function.
  - body.txt -> Contain the mail message. You will have to edit (check use guide, up)
  - lista.txt -> One of the two files that you can use for contain the users data.
  - main.py -> The main excecutable.
  - readex.py -> Contain functions used for read the .xlsx file and process the user data.

Own Functions:
  - get_message() -> Open body.txt file and separate the subject and body for the email.
  
  - Open_Book() -> Load the .xlsx file that your enter in a input and return the sheet.
  
  - maxRow(sheet) -> return the num of rows that have in the excel sheet.
  
  - Obtain_Users(sheet) -> Obtain all the data of the users and return a array with dicts of the user data.
  
  - add_us(user, passwd, desc) -> Run a linux command for add users, using 3 variables as arguments.
    user: user id,
    passwd: user password,
    desc: user comment, a description basically.
    
  - send_mail(receiver, name, surname, user, passwd) -> Send a email using smtplib, ssl and processing the body.txt message.
    receiver: the mail receiver
    name: name of the user owner
    surname: surname of the user owner
    user: user id
    passwd: user password

Modules and libraries used: smtplib, ssl, system, os, subprocess, email.message, re, dotenv, time, string.

The program have several things to improve (ignoring that the code is a bit disorganized, the spainglish, etc etc). A example to add: include the user groups.
That's why I leave it here so you can improve it if you want :).
  
