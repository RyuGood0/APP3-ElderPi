import json
def age_de_mort(dic):
    """
    Fonction qui lit l'age de mort d'un individu à partir du fichier countries_dict.txt
    """
    f = open("countries_dict.json", "r")
    raw_dict = json.load(f)
    print(raw_dict)

    
