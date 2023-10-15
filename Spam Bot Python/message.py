from parle_a_ma_place import *

def text():
    message = input("Quelle phrase voulez-vous écrire : ")
    time.sleep(1)
    print("Enregistrement ...")
    time.sleep(2)
    print("Vous avez choisi : " + message)
    time.sleep(1)
    nombre_message.talk_for_me(message)