import os
from crypto import *

def creer_mdp(vars):
    # On créer un fichier auth.sess et on y écrit le hash du mot de passe
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in vars.values())

    with open(savefile, 'w') as f:
        f.write(hashing(mdp))

def is_mdp():
    # On vérifie si le fichier auth.sess existe
    return os.path.exists("auth.sess")

def verifier_mdp(mdp):
    # On vérifie si le mot de passe est correct
    savefile = "auth.sess"

    try:
        with open(savefile, 'r') as f:
            if hashing(mdp) == f.read():
                return True
            else:
                return False
    except:
        return False

def enregistrer_code(vars, mdp):
    # On créer un fichier secret.txt et on y écrit le code en utilisant le mot de passe
    savefile = "secret.txt"

    mdp = ''.join(str(arg) for arg in mdp.values())

    code = ''.join(str(arg) for arg in vars.values())
    with open(savefile, 'w') as f:
        f.write(encode(mdp, code))

def lire_code(mdp):
    # On lit le code en utilisant le mot de passe
    mdp = ''.join(str(arg) for arg in mdp.values())
    if verifier_mdp(mdp):
        savefile = "secret.txt"

        with open(savefile, 'r') as f:
            return decode(mdp, f.read())