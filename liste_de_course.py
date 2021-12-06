def créer_liste_de_course():
    filepath = "liste_de_course.txt"
    with open(filepath, "w") as f:
        f.write("")

def ajouter_produit(produit):
    filepath = "liste_de_course.txt"
    with open(filepath, "a") as f:
        f.write(produit + "\n")

def lister_produits():
    filepath = "liste_de_course.txt"
    product_list = []
    with open(filepath, "r") as f:
        for line in f:
            product_list.append(line.strip())

    return product_list

def supprimer_produit(produit):
    filepath = "liste_de_course.txt"
    with open(filepath, "r") as f:
        lines = f.readlines()
    with open(filepath, "w") as f:
        for line in lines:
            if line.strip() != produit:
                f.write(line)