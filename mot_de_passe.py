from crypto import hashing

def creer_mdp(*args):
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in args)

    with open(savefile, 'w') as f:
        f.write(hashing(mdp))

def verifier_mdp(*args):
    savefile = "auth.sess"

    mdp = ''.join(arg for arg in args)

    with open(savefile, 'r') as f:
        if hashing(mdp) == f.read():
            return True
        else:
            return False

def enregistrer_code(code):
    savefile = "secret.txt"

    with open(savefile, 'w') as f:
        f.write(code)

def lire_code(*args):
    if verifier_mdp(*args):
        savefile = "secret.txt"

        with open(savefile, 'r') as f:
            return f.read()