import pyautogui
import time
from plyer import notification
import datetime
import pywhatkit
print("--------HELLO!-------\n"
      "WELCOME TO AUTO-TYPE")
print("Press 1 for Auto-typing\n"
      "Press 2 for sending mesaage on whatsapp to particular number\n"
      "Press 3 to exit")
choice=input("Enter Your Choice:\n")
if choice=='1':

    user_name=input("Enter Your Name:\n")
    print(f"{user_name.capitalize()} Please Follow The Given Instructions\n")
    how_many=int(input("Enter how many times you wanna print the given message:  \n"))
    main_message=input("Enter your message here: \n")
    pause=int(input("Enter after how many seconds the message should be repeated: \n"))
    while how_many > 0:
        time.sleep(pause)
        pyautogui.typewrite(main_message)
        time.sleep(3)
        pyautogui.press('enter')
        title1="Message"
        message1=f"Sent at {datetime.datetime.now()}"
        notification.notify(title=title1, message=message1, app_icon=None, timeout=2, toast=False)
        how_many=how_many-1
elif choice=='2':
    user_name = input("Enter Your Name:\n")
    print(f"{user_name.capitalize()} Please Follow The Given Instructions\n")
    print("It requires good internet connection and your should be signed in to your whatsapp account and your browser should be open")
    number=input("Enter number to which you want to send message:\n")
    a=f"+91{number}"
    whatsapp=input("Enter message you want to send:\n")
    hours=int(input("Enter hours:\n"))
    minutes=int(input("Enter minutes:"
                      "\n"))
    pywhatkit.sendwhatmsg(a,whatsapp,hours,minutes)
    title2 = "WHATSAPP"
    message2 = "WHATSAPP MESSAGE SENT"
    notification.notify(title=title2, message=message2,
                        app_icon=None, timeout=3, toast=False)
elif choice=='3':
    pass
else:
    print("Invaild Input  :(")