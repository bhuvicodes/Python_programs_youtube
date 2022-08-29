import os
shutdown = input("Do you want to shutdown (yes / no) : ")
if shutdown == "yes":
    os.system("shutdown /s /t 1")
else:
    print("shutdown is not requested")