import rhasspy
from sense_hat import SenseHat

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini")
print("Apprentissage terminé.")

rhasspy.text_to_speech("Assistant prêt à l'usage.")

while True:
    try:
        intent = rhasspy.speech_to_intent()
        print(intent)
    except:
        pass