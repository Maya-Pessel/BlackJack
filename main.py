from fonction import *

# ############# REGLES ###############
# Créer les joueurs
# Definir les cartes
# Les joueurs choisissent le montant de leurs mises
# Le croupier distribue 2 cartes a chacun des joueurs (le croupier conserve une carte face cachée)
# Donner des valeurs au cartes
# As = 1 ou 11
# Les joueurs choisissent de tirer une carte ou pas
# Possibilité de miser plus avant de piocher
# Afficher la carte cacher du croupier
# Si le croupier a <= 16 alors obliger de piocher
# Si plus élevé que 21 = perdu
# Si le croupier a + de 21 tout les joueurs qui n'on pas depasser 21 gagnent
# Etape 6, répartition des gains (le joueur perd si - que le croupier)
# Si gagnant : gain = 1x la mise de depart
# Si black jack ( 21 ) gain = 1,5x mise de depart
# Si paire, possibilité de séparer ses cartes pour former deux mains + obligation de doubler sa mise

# joueurs = [["Maya", 21, 50, [2, 3], ["Fares", 23, 100, [12, 8]]
creation_cartes()
nb_joueur = int(input("Combien de joueurs participant a la partie ? "))
joueurs = creation_joueur(nb_joueur)
while True:
    miser(joueurs)
    distribuer_2carte(joueurs)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    afficher_jeux(joueurs)
    input()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    # Premier tour pour verifier as
    for joueur in joueurs:
        if joueur[0] != "Croupier":
            choix_as(joueur)

    # Tour des joueurs
    tour_joueurs(joueurs)

    # Tour du croupier
    tour_croupier(joueurs[0])
    print()
    print("~~~~~ La carte du croupier est révélée ~~~~~")
    afficher_jeux(joueurs, True)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    # Calcul des resultats
    print()
    print("~~~~~~~~~~~~~~~~~ Résultats ~~~~~~~~~~~~~~~~~")
    print()
    resultats(joueurs)
    reinitialiser(joueurs)
    if input("Voulez vous rejouer ? ") == "Non":
        break
