# Creator Lissan Koirala
# Date of Creation 18/02/2019

import random # For generating ramdom codes
import time
import os
# To send email
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase  #  This is to send the user his code and the encrypted message
from email import encoders  #  Encodes the message that is being sent to the user

print(" \n \n \nEncrytion / Decrytion") # This is for the attraction
print("-"*119) # This is to design
print("Your Encrytion code will be saved in the Decryption_Code.txt")
print("-"*119)

# Generating a Key and Saving It !
key_num = ""
numbers_code = ['1','2','3','4','5','6','7','8','9'] # This are the possible numbers in the key
for i in range(5):
  index = random.randint(0,8) # Generates the random number
  key_num += numbers_code[index]  # And adds the number into the key

key_alpha = ""
alpha_code = ['A','a','@','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']  # This are the possible alphabets in to key
for i in range(5):
  index = random.randint(0,52) # Generates a random number
  key_alpha += alpha_code[index] # Adds the random alphabets into the key

key_print = key_num[0] + key_alpha[0] + key_num[1] + key_alpha[1] + key_num[2] + '//' + key_alpha[2] + key_num[3] + key_alpha[3] + key_num[4] + key_alpha[4]                     

f = open("Decryption_Code.txt","w") # Creates a file to store the Decrption Code
f.write(key_print) # Writes the code into file
f.close()  # Closes the file

# Key Distributer
key_stage_1 = int(key_print[0]) 
key_stage_2 = int(key_print[2])
key_stage_3 = int(key_print[4]) # Takes out the real key form the key that is printed out
key_stage_4 = int(key_print[8])
key_stage_5 = int(key_print[10])



# Getting the message from the user which is going to be encrypt
message = input("Enter a Message to Encrypt : ")  # User enters the message to be encrypted
print("Your key is : ",key_print) # Gives the user the key

##############    Message starts to Encrypt    ##############

# Encryption Level 1
encrypted_stage_1 = ""
for letter in message: 
  encrypted_stage_1 += chr(ord(letter)+ key_stage_1) 

# Encryption Level 2
encrypted_stage_2 = ""
for letter in encrypted_stage_1: 
  encrypted_stage_2 += chr(ord(letter)+ key_stage_2) 

# Encryption Level 3
encrypted_stage_3 = ""
for letter in encrypted_stage_2: 
  encrypted_stage_3 += chr(ord(letter)+ key_stage_3) 

# Encryption Level 4
encrypted_stage_4 = ""
for letter in encrypted_stage_3: 
  encrypted_stage_4 += chr(ord(letter)+ key_stage_4) 

# Encryption Level 1
encrypted_stage_5 = ""
for letter in encrypted_stage_4: 
  encrypted_stage_5 += chr(ord(letter)+ key_stage_5) 

# Final Substracting, Adding, Multiplying, Dividing all the key_Stages
final_stage_key = key_stage_1 + key_stage_2 - key_stage_3 * key_stage_4 // key_stage_5
final_stage = ""
for letter in encrypted_stage_5: 
  final_stage += chr(ord(letter)+ final_stage_key) 
encrypted = final_stage

########### Message has been Encrypted  ##############

print("Your Messaged has been Encrypted and saved in the Encrypted_Message file,")
print("-"*119)
print("\nYou will need this code to Decrypt this Message\nCode : ",key_print)
print("-"*119)

# Saving the encrypted message in a file
f = open('Encrypted_Message.txt','w')  # Saves the Encrypted Message in to a file
f.write(encrypted) # Writes into the file
f.close()  # Close the file

# Sends the Code and the Message to the users email ID       
print("If you want me to send this Code and Encrypted Message to your email with a high security then enter your email address below : ")
email_to = input("Your Email ID : ")
print("-"*119)
if email_to != "":
  try:
    fromaddr = "SENDER_EMAIL"
    toaddr = email_to
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Your Encryption Details"
    mes = "Hi There,\nYou just Encrypted something from My Software.\nHere is the following code which you will need to Decrypt your Message!"
    mes1 = mes + "\nCode : "
    mes2 = mes1 + key_print
    mes = mes2 + "\n\nYour Sincerely\nOrganisation"
    body = mes3
    msg.attach(MIMEText(body, 'plain')) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "SENDER_PASSWORD") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    print("Your Code and Encrypted Message Has Sucessfully sent to ",email_to)
    print("-"*119)
  except: # If the email was incorrect or if the user didn't want to recieve email
    print("There was error sending an email to you, Looks you provided an incorrect email, Try:\n-Re-encrypting your message again and then input a right email\n-Save this code somewhere you can acess")
    print("-"*119)
    print("GENTLE WARNING - \"IT'S CURTIAL TO HAVE THIS CODE WHILE DECRYPTING THE MESSAGE,\nIF YOU LOST IT YOU HAVE TO PAY ME FOR THE CODE")
    print("-"*119)
    print("Code : ",key_print)
    print("-"*119)

time.sleep(3)
print("ATTENTION, THIS SOFTWARE WILL CLOSE IN 10 SECONDS")  # States that the file is being closed
time.sleep(10)



            
