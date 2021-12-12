import json
# import rhasspy
# from sense_hat import SenseHat




def age_de_mort(dic):
    """
    Fonction qui lit l'age de mort d'un individu à partir du fichier countries_dict.txt
    """
    f = open("countries_dict.json", "r")
    raw_dict = json.load(f)
    dic['pays'] = dic['pays'].capitalize() 
    
    if dic['sexe'] == 'une femme': sexe = 3 
    else: sexe = 5
    
    age = float(dic['age'])
    pays = dic['pays']

    #if age > 87 : rhasspy.text_to_speech("Vous êtes déjà censés être morts .")

    difference_age = float(raw_dict[pays][sexe]) - age
    difference_age = round(difference_age, 2)
    
    if difference_age < 0 : print("Vous êtes déjà censés être morts .")
    #rhasspy.text_to_speech("Vous avez " + str(difference_age) + " ans avant de mourir.")
    
    else : print("Vous avez " + str(difference_age) + " ans avant de mourir.")
    #rhasspy.text_to_speech("Votre pays est numéro" + str(raw_dict[pays][sexe-1]) + 'mondial ')

    print("Votre pays est numéro " + str(raw_dict[pays][sexe-1]) + ' mondial ')

age_de_mort({'sexe': 'une femme', 'age' : '69', 'pays' : 'niger'})