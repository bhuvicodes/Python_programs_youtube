import pywhatkit

PH_NUM = input("Enter the phone number: ")#with country code
MSG = input("Enter the message: ")
HR = int(input("Enter hour: ")) #24 hour format
MIN = int(input("Enter minutes: "))

pywhatkit.sendwhatmsg(PH_NUM, MSG, HR, MIN)
