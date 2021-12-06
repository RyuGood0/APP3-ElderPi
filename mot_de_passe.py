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