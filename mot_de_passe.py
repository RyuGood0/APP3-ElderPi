from crypto import *

def creer_mdp(vars):
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in vars.values())

    with open(savefile, 'w') as f:
        f.write(hashing(mdp))

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

def enregistrer_code(vars):
    savefile = "secret.txt"

    mdp = ''.join(arg for arg in vars.values() if arg in ["mdpun", "mdpdeux", "mdptrois"])

    code = ''.join(arg for arg in vars.values() if not (arg in ["codeun", "codedeux", "codetrois"]))
    with open(savefile, 'w') as f:
        f.write(encode(mdp, code))

def lire_code(vars):
    mdp = ''.join(arg for arg in vars.values() if arg in ["mdpun", "mdpdeux", "mdptrois"])
    if verifier_mdp(mdp):
        savefile = "secret.txt"

        with open(savefile, 'r') as f:
            return decode(mdp, f.read())