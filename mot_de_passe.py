from crypto import *

def creer_mdp(*args):
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in args)

    with open(savefile, 'w') as f:
        f.write(hashing(mdp))

def verifier_mdp(mdp):
    savefile = "auth.sess"

    with open(savefile, 'r') as f:
        if hashing(mdp) == f.read():
            return True
        else:
            return False

def enregistrer_code(code, *args):
    savefile = "secret.txt"

    mdp = ''.join(arg for arg in args)

    with open(savefile, 'w') as f:
        f.write(encode(mdp, code))

def lire_code(*args):
    mdp = ''.join(arg for arg in args)
    if verifier_mdp(mdp):
        savefile = "secret.txt"

        with open(savefile, 'r') as f:
            return decode(mdp, f.read())