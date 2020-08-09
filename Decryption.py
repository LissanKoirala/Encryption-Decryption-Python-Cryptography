# Creator Lissan Koirala
# Date of Creation 18/02/2019

from gtts import gTTS  # This is to read the message
from playsound import playsound  # This plays the sound
import time  # To delay the program

print("")
print("")
print("Encrytion / Decrytion") # This is For Attractions
print("-"*119) # This is a Design
print("HERE YOU DECRYPT YOUR ENCRYPTED MESSAGE DONE FROM LISSAN'S SOFTWARE")
print("-"*119)

# Decrypt
decrypted_message = "" # Initially the message is empty
encrypted_message = input("Your Encrypted Message or the file name with the extension .txt : ") # Here the user writes the file name or the Encrypted Message to be Decrypted
length = len(encrypted_message) - 4 # This takes out the .txt form the input
file_name = encrypted_message[length:] # Take the .txt if it was a file name that was provided
if file_name == ".txt":   # IF the input was a file name then we open that file and read what's inside it
  while True:
    try:
      g = open(encrypted_message,'r')  # Opening the file
      encrypted_message = g.read()   # Reading the file
      g.close()   # Closing the file
      break
    except:
      print("You Have enterd an wrong file, please recheck and write it Exactly the Same way with the extension .txt included! :)")
      print("Please Try : Encrypted_Message.txt")   #  If the file name was wrong then the user re-inputs the message
      encrypted_message = input("Your Encrypted Message or the file name with the extension .txt : ")
     
key_user = input("Your key or the file name with the extension .txt: ")   # Here the user inputs the key that was given when he encrypted the message
length = len(key_user) - 4 # If the input is file name
file_name = key_user[length:] # Take the .txt if it was a file name that was provided
if file_name == ".txt":
  while True:
    try:
      g = open(key_user,'r')  # Opens the file
      key_user = g.read()  # Reads the file
      g.close()  # Closes the file
      break
    except:
      print("You Have enterd an wrong file, please recheck and write it Exactly the Same way with the extension .txt included! :)")
      print("Please Try : Decrytion_Code.txt")  # If the file is wrong, user inputs again
      key_user = input("Your key : ")


# Key Distributer
key_stage_1 = int(key_user[0])
key_stage_2 = int(key_user[2])
key_stage_3 = int(key_user[4])   # The real keys are taken from the input, some of them are just to look attractive
key_stage_4 = int(key_user[8])
key_stage_5 = int(key_user[10])

################   Starting to decrypt   ################

# Final Substracting, Adding, Multiplying, Dividing all the key_Stages
final_stage_key = key_stage_1 + key_stage_2 - key_stage_3 * key_stage_4 // key_stage_5
final_stage = ""
for letter in encrypted_message: 
  final_stage += chr(ord(letter)- final_stage_key) 

# Decrypted Message Level 5
decryption_stage_5 = ""
for letter in final_stage: 
  decryption_stage_5 += chr(ord(letter)- key_stage_5) 

# Decrypted Message Level 4
decryption_stage_4 = ""
for letter in decryption_stage_5: 
  decryption_stage_4 += chr(ord(letter)- key_stage_4) 

# Decrypted Message Level 3
decryption_stage_3 = ""
for letter in decryption_stage_4: 
  decryption_stage_3 += chr(ord(letter)- key_stage_3) 

# Decrypted Message Level 2
decryption_stage_2 = ""
for letter in decryption_stage_3: 
  decryption_stage_2 += chr(ord(letter)- key_stage_2) 

# Decrypted Message Level 1
decryption_stage_1 = ""
for letter in decryption_stage_2: 
  decryption_stage_1 += chr(ord(letter)- key_stage_1) 
decrypted_message = decryption_stage_1

############ Decryption ends here ############

print("Your Decrypted Message : ", decrypted_message)  # Shows the decrypted Message
print("-"*119)

x = input("Do you want to hear you Decrypted File? (Yes Or No) ")  # Asking if he wants to hears the message
print("-"*119)
if x in ["y","Y","yes","Yes"]:
  speech = gTTS(text = str(decrypted_message), lang = "en", slow = False) # This makes the file
  speech.save("decrypt.mp3")  #  Saves the file 
  playsound("decrypt.mp3")  # Plays the file
else:
  pass

time.sleep(3)
print("ATTENTION, THIS SOFTWARE WILL CLOSE IN 10 SECONDS") # Indicates that the file is closing soon
time.sleep(10) # After ten seconds the file closes
