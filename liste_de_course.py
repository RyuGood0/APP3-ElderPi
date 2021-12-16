def créer_liste_de_course():
    # On créer un fichier liste_de_course.txt
    filepath = "liste_de_course.txt"
    with open(filepath, "w") as f:
        f.write("")

def ajouter_produit(produit):
    # On ajoute le produit à la liste de course
    filepath = "liste_de_course.txt"
    with open(filepath, "a") as f:
        f.write(produit + "\n")

from collections import Counter
def lister_produits():
    # On lit la liste de course et on renvoie un dictionnaire avec le nombre de fois qu'un produit est présent
    filepath = "liste_de_course.txt"
    with open(filepath, "r") as f:
        product_list = f.read().splitlines()

    return Counter(product_list)

def supprimer_produit(produit):
    # On supprime le produit de la liste de course
    filepath = "liste_de_course.txt"
    with open(filepath, "r") as f:
        lines = f.readlines()
    with open(filepath, "w") as f:
        for line in lines:
            if line.strip() != produit:
                f.write(line)