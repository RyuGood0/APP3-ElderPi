import rhasspy
from sense_hat import SenseHat
from mot_de_passe import *
from age_de_mort import age_de_mort
from playmusic import *
from liste_de_course import *
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

		if started_session == False and intention == "Lancement":
			print("Lancement de la session.")
			started_session = True
			rhasspy.text_to_speech("Bonjour, je suis votre assistant. Veuillez enregistrer votre mot de passe pour la session.")
		elif started_session == True:
			if saved_password == None and is_mdp():
				if intention == "EnregistrerMDP":
					if verifier_mdp(''.join(arg for arg in ntent["variables"].values())):
						saved_password = intent["variables"]
						rhasspy.text_to_speech("Mot de passe enregistré, vous pouvez commencer.")
						print("Vous pouvez commencer")
					else:
						rhasspy.text_to_speech("Mot de passe invalide")
						print("Mot de passe invalide")
			elif saved_password == None and not is_mdp():
				if intention == "NouveauMDP":
					creer_mdp(intent["variables"])
					saved_password = intent["variables"]
					rhasspy.text_to_speech("Mot de passe enregistré, vous pouvez commencer.")
					print("Vous pouvez commencer")
			else:
				if intention == "NouveauCode":
					enregistrer_code(intent["variables"], saved_password)
				elif intention == "LireCode":
					lire_code(intent["variables"], saved_password)
				elif intention == "AgeDeMort":
					age_de_mort(intent["variables"])
				elif intention == "AjoutListe":
					objet = intent["variables"]["objet"]
					ajouter_produit(objet)
					rhasspy.text_to_speech(f"{objet} ajouté")
				elif intention == "LireListe":
					rhasspy.text_to_speech(''.join(objet + " " for objet in lister_produits()))
				elif intention == "SupprObjet":
					objet = intent["variables"]["objet"]
					supprimer_produit(objet)
					rhasspy.text_to_speech(f"{objet} supprimé")
				elif intention == "JouerMusique":
					playmusic()
			if intention == "Fin":
				saved_password = None
				started_session = False
				rhasspy.text_to_speech("Fin de session, au revoir")

	except Exception as e:
		if e == KeyboardInterrupt:
			rhasspy.text_to_speech("Au revoir et a bientot.")
			break
		else:
			print("La phrase n'a pas été")
			print(e)
