import rhasspy
from sense_hat import SenseHat
from mot_de_passe import *
sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini")
print("Apprentissage terminé.")

rhasspy.text_to_speech("Assistant prêt à l'usage.")

started_session = False
saved_password = None

while True:
	try:
		intent = rhasspy.speech_to_intent()
		print(intent)

		intention = intent["name"]

		if intention == "Lancement":
			started_session = True
			rhasspy.text_to_speech("Bonjour, je suis votre assistant. Veuillez enregistrer votre mot de passe pour la session.")

		if started_session == True:
			if saved_password == None:
				if intention == "EnregistrerMDP":
					saved_password = intent["variables"]
			else:
				if intention == "NouveauMDP":
					creer_mdp(intent["variables"])
				elif intention == "NouveauCode":
					enregistrer_code(intent["variables"], saved_password)
				elif intention == "LireCode":
					lire_code(intent["variables"], saved_password)
			if intention == "Fin":
				started_session = False

	except Exception as e:
		if e == KeyboardInterrupt:
			break
		else:
			print("La phrase n'a pas été")
