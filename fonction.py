import random


# Création des joueurs
def creation_joueur(nb_joueur):
    joueurs = [["Croupier", 0, 0, []]]
    while nb_joueur != 0:
        reponse_nom = input("Quel est ton nom ? ")
        if reponse_nom != "":
            nb_joueur = nb_joueur - 1
            age_int = 0
            while age_int == 0:
                age_str = input(reponse_nom + " quel est ton age ? ")
                try:
                    age_int = int(age_str)
                except:
                    print("Erreur, vous devez entrer un nombre.")
            if age_int < 18:
                print("Vous etes mineur, vous ne pouvez pas jouer.")
            else:
                joueurs.append([reponse_nom, age_int, 0, []])
    return joueurs


# Création paquet de carte
cartes = []


def creation_cartes():
    paquet_carte = 6
    for p in range(paquet_carte):
        type_carte = 4
        for t in range(type_carte):
            valeur_carte = 13
            for v in range(valeur_carte):
                if v > 9:
                    v = 9
                cartes.append(v+1)
    random.shuffle(cartes)
    del cartes[0:5]


def choix_as(joueur):
    for idx, carte in enumerate(joueur[3]):
        if carte == 1:
            choix = int(input(joueur[0] + " vous avez un as. Voulez vous choisir la valeur 1 ou 11 ? "))
            if choix == 11:
                joueur[3][idx] = 11


# Création des mises
# joueurs = [["Croupier", age, mise]["Fares", age, mise], ["Yacine", age, mise]]
def miser(joueurs):
    for joueur in joueurs:
        if joueur[0] != "Croupier":
            mise = int(input(joueur[0] + " combien voulez vous miser ? "))
            joueur[2] = mise
    # return joueurs


# Distribuer cartes
def recuperer_une_carte():
    return cartes.pop(0)


# joueur = [nom, age, mise, [carte1, carte2]]
def distribuer_2carte(joueurs):
    for joueur in joueurs:
            joueur[3].append(recuperer_une_carte())
            joueur[3].append(recuperer_une_carte())
    # return joueurs



def distribuer_1carte(joueur):
    joueur[3].append(recuperer_une_carte())


def total_carte(joueur):
    sum(joueur[3])
    return sum(joueur[3])


# Afficher une seule carte du croupier
def afficher_jeux(joueurs, tourcroupier=False):
    for idx, joueur in enumerate(joueurs):
        texte = f"Joueur : {joueur[0]} "
        if tourcroupier:
            texte += f" main : {joueur[3]} score : {total_carte(joueur)}"
        elif idx == 0:

            texte += "main : " + str(joueur[3][1])
        else:
            texte += f" mise : {joueur[2]}, main : {joueur[3]} score : {total_carte(joueur)}"
        print(texte)


# Tour des joueurs

def plus_egal21(joueur):
    total = sum(joueur[3])
    if total >= 21:
        return True
    return False


def tour_joueurs(joueurs):
    for joueur in joueurs:
        if joueur[0] != "Croupier":
            if plus_egal21(joueur) is False:
                choix = (input(joueur[0] + " que voulez vous faire : doubler(1), piocher(2), stop(3) ? "))
                if choix == "1":
                    joueur[2] = joueur[2] * 2
                    distribuer_1carte(joueur)
                    choix_as(joueur)

                if choix == "2":
                    while True:
                        distribuer_1carte(joueur)
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        afficher_jeux(joueurs)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()
                        choix_as(joueur)
                        if plus_egal21(joueur) is True:
                            break
                        choix_piocher = (input(joueur[0] + " voulez vous une autre carte ? (Oui/Non) "))
                        if choix_piocher == "Oui" or "oui" or "o":
                            afficher_jeux(joueurs)
                        if choix_piocher == "non" or "Non" or "n":
                            break
                        # if choix == "separer":


# Tours croupier
def tour_croupier(croupier):
    choix_as(croupier)
    while sum(croupier[3]) <= 16:
        distribuer_1carte(croupier)
        choix_as(croupier)
        print()
        print("~~~~~~~~~~~~ Le croupier pioche ~~~~~~~~~~~~")
        print()


def resultats(joueurs):
    for joueur in joueurs:
        score_joueur = sum(joueur[3])
        score_croupier = sum(joueurs[0][3])

        if score_joueur == 21:
            print(joueur[0] + str(" vous faite un Black Jack. Bien joué ! Vous gagnez " + joueur[2] + "$."))
            if joueur[0] != "Croupier":
                joueur[2] *= 2.5

        elif score_croupier < score_joueur < 21:
            # Si les joueurs sont superieur au croupier et inferieur a 21
            print(joueur[0] + " vous avez battu le croupier ! Vous gagnez " + str(joueur[2]) + "$.")
            if joueur[0] != "Croupier":
                joueur[2] *= 2

        elif score_joueur < score_croupier <= 21:
            # Si le croupier est superieur au joueurs et inferieur ou égal a 21
            print(joueur[0] + " le croupier vous a battu !")
            if joueur[0] != "Croupier":
                joueur[2] = 0

        elif score_joueur > 21:
            # Si les joueurs sont superieur a 21 et que le croupier inferieur ou égal a 21
            print(joueur[0] + " vous avez dépasser 21... Dommage !")
            if joueur[0] != "Croupier":
                joueur[2] = 0

        elif score_croupier > 21 >= score_joueur:
            # Si le croupier est superieur a 21 et que les joueurs sont inferieur ou égal a 21
            print(joueur[0] + " le croupier a depasser 21, vous avez gagné ! Vous gagnez " + str(joueur[2]) + "$.")
            if joueur[0] != "Croupier":
                joueur[2] *= 2

        elif 21 >= score_joueur == score_croupier <= 21:
            # Si les joueurs et le croupier sont égal et inferieur ou égal a 21
            if joueur[0] != "Croupier":
                print(joueur[0] + " egalité avec le croupier ! Vous récupez votre mise.")


def reinitialiser(joueurs):
    for joueur in joueurs:
        joueur[3].clear()
        joueur[2] = 0
