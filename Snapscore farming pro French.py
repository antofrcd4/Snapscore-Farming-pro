import time
import pyautogui
import cv2
import keyboard
print("************ INSTRUCTIONS : ************")
print("Bienvenue dans snapscore farming pro par a_frcd4")
print("Le programme va envoyer des photos en continu à quelqu'un que vous aurez choisi. Le destinataire sera le premier dans votre liste de contacts lorque le programme entrera le nom que vous aurez donné. En cas de problème, changez le nom de cette personne sur snap")
print("Il est déconseillé de dépasser les valaurs par défaut de temps et d'interval, car vous risquez un ban perm. Le programme est conçu pour aller à la limite du ban.")
print("Avant de démarer, assurez vous d'être en mode sombre et de bien avoir la fenêtre 'snapchat, now on the web' en plein écran, ou l'application de bureau. Vous devez voir apparaitre un appareil photo, qui doit être entièrement visible au début du programme")
print("Le programme requiert python, OpenCV2 et pyautogui. Tapez 'pip install pyautogui' et 'pip install keyboard' dans votre terminal si vous ne possédez pas encore ces deux modules")
print("Pour arréter le programme avant sa fin, appuyez longuement sur échap, ou mettez votre souris en haut à gauche de l'écran")
print("Avis et rapports de bug à antfourcade@gmail.com")
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
                print("Merci d'attendre 20 secondes pendant que la page se rafraichit...")
                time.sleep(20)
        else:
            print("Vous avez arrété le programme")
            break

def main() :

    count = input("Nombre de snaps à envoyer (rythme par défaut : environs 3000 par heure (par défaut: 1000000): ")
    interval = input("Temps entre chaque snap (par défaut: 0.2): ")
    delay = input("Délai entre les actions (par défaut: 0.1): ")
    user: str = ""
    while not user:
        user = input(f"Destinataire (Les caractères spéciaux (é,è,ç, etc...) ne sont PAS acceptés, modifiez le nom de votre destinataire si besoin) : ")
    
    send_snaps(count, interval, delay, user)
    print("**********Sucessfully ended************")
    print("Merci d'avoir utilisé SnapFarming pro !! Vos retours m'intérèssent, donc contactez moi sur antfourcade@gmail.com si vous trouvez des bugs où améliorations possibles")
    time.sleep(300)

main()
