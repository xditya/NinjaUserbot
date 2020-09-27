  
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print("""processing.......""")

API_KEY = '1754367'
API_HASH = "231b8cc6cca12ee51a85cf543321f476"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"**Here is your TELEGRAM STRING SESSION**👇\n(tap to copy) \n\n `{session}`")
      print("You Telegram String session has been successfully stored in your Telegram Saved Messages. Please check your Saved Messages!")
      print("Store it safe!!")
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct  country code")
   print ("")
   continue
  break
