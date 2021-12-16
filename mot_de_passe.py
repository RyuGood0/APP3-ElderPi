import os
from crypto import *

def creer_mdp(vars):
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in vars.values())

    with open(savefile, 'w') as f:
        f.write(hashing(mdp))

def is_mdp():
    return os.path.exists("auth.sess")

def verifier_mdp(mdp):
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
    savefile = "secret.txt"

    mdp = ''.join(str(arg) for arg in mdp.values())

    code = ''.join(str(arg) for arg in vars.values())
    with open(savefile, 'w') as f:
        f.write(encode(mdp, code))

def lire_code(mdp):
    mdp = ''.join(str(arg) for arg in mdp.values())
    if verifier_mdp(mdp):
        savefile = "secret.txt"

        with open(savefile, 'r') as f:
            return decode(mdp, f.read())