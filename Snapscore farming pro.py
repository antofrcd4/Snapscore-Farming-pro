import time
import pyautogui
import cv2
import keyboard
print("************ INSTRUCTIONS : ************")
print("Welcome in Snapscore farming pro designed by a_frcd4")
print("The program will send a lot of snaps to someone you choosed (the first in your sharing list when you type the name of the recipient). If you've got a problem, change the name of your friend on snap")
print("It is not advisable to exceed the default values of intervale and time, because you risk a ban")
print("Make sure you're in DARK MODE. If you get an error, make sure the window 'Snapchat, now on the web' or the desktop app is in full screen, and there is nothing else on the image of camera in the center of the screen")
print("Use the english (US) version of snapchat, else, that won't work. If you want to stay in French, use the french version of this program")
print("OpenCV, and pyautogui and keyboard from pip are needed. Just type 'pip install pyautogui' and 'pip install keyboard' in your prompt")
print("To kill the program, press escape for a long time or put your mouse in the left top corner of your screen")
print("Feedback and bug reports at antfourcade@gmail.com")
print("*****************ENJOY******************")
print("")
def send_snaps(count: int, interval: float, delay: float, user: str) :
    """Send snaps on snapchat using mouse movements.
    :param count: The amount of snaps to send
    :param interval: Time between each snap
    :param delay: The delay between each step/action
    :param user: The username of the recipient whom the snaps will be sent to
    """
    #DEFAULT VALUES
    if count=='' or type(count)!= int:
        count=1000000
    if interval=='' or type(interval)!= float:
        interval=0.2
    if delay=='' or type(delay)!= float:
        delay=0.1
    #START OF THE PROCESS
    
    for i in range(count):
        if keyboard.is_pressed('esc')==False:
            time.sleep(interval)
            print(f"Snap #{i + 1}")
            #INITIALISATION BY PHOTO-FOUNDER
            if i==0:
                p1 = pyautogui.locateCenterOnScreen("starting.png", confidence=0.9)
                a1, b1 = p1
                pyautogui.click(a1, b1)
                time.sleep(3)
                p2 = pyautogui.locateCenterOnScreen("photo_button.png", confidence=0.9)
                a2, b2 = p2
                pyautogui.click(a2, b2)
                time.sleep(delay)
                p3 = pyautogui.locateCenterOnScreen("SendTo_button.png", confidence=0.9)
                a3, b3 = p3
                pyautogui.click(a3, b3)
                time.sleep(1)
                pyautogui.write(user)
                time.sleep(delay)
                p4 = pyautogui.locateCenterOnScreen("Results.png", confidence=0.9)
                a4, b4 = p4
                b4 = b4+30
                pyautogui.click(a4, b4)
                time.sleep(delay)
                p5 = pyautogui.locateCenterOnScreen("Send_button.png", confidence=0.9)
                a5, b5 = p5
                pyautogui.click(a5, b5)
            #CLICKING
            pyautogui.click(a2, b2)
            time.sleep(delay)
            pyautogui.click(a3, b3)
            time.sleep(delay)
            pyautogui.write(user)
            pyautogui.click(a4, b4)
            time.sleep(delay)
            pyautogui.click(a5, b5)
            time.sleep(interval)
            #refreshing after 500 snaps sent
            if i%500==0 and i!=0:
                pyautogui.keyDown('fn')
                pyautogui.press('f5')
                pyautogui.keyUp('fn')
                pyautogui.press('f5')
                print("Please wait 20 secondes while the window refresh")
                time.sleep(20)
        else:
            print("You killed the program")
            break

def main() :

    count = input("Amount of snaps to send (default: 1000000): ")
    interval = input("Time between each snap (default: 0.2): ")
    delay = input("Delay between actions (default: 0.1): ")
    user: str = ""
    while not user:
        user = input(f"Recipient (é,è,ç, etc... are NOT ACCEPTED) : ")
    
    send_snaps(count, interval, delay, user)
    print("**********Sucessfully ended************")
    print("Thank you to use SnapFarming !! Feedback are very important for me, so contact me at antfourcade@gmail.com for all bugs or ameliorations you found")
    
    time.sleep(300)
main()
