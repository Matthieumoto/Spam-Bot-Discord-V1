from parle_a_ma_place import *

def talk_for_me(text):
    c = 0
    x = int(input("Combien de messages voulez vous envoyez : "))
    time.sleep(1)
    print("Enregistrement ...")
    time.sleep(2)
    print("Vous avez choisi d'envoyer", x,"fois ")
    time.sleep(1)
    print("Préparez vous ...")
    time.sleep(1)
    cinq_secondes.decompte()
    pyautogui.hotkey('alt', 'tab') 
    pyautogui.click(1040, 1000)
    time.sleep(2)

    for i in range(x):
        time.sleep(0.5)
        pyperclip.copy(text)  
        pyautogui.hotkey('ctrl', 'v') 
        pyautogui.press('enter')
        c = c + 1
        if c == x:
            time.sleep(2)
            pyautogui.hotkey('alt', 'tab') 
            print("Vous avez fini")