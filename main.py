import random


class Contact:
    def __init__(
        self, prenom: str, nom: str, numero: str, email: str, identifiant: str
    ) -> None:
        self.prenom = prenom
        self.nom = nom
        self.numero = numero
        self.email = email
        self.identifiant = identifiant

    def full_name(self):
        return f"{self.nom.upper()} {self.prenom}"

    def afficher(self):

        print(f"\n--- Infos de '{self.full_name()}' ---")
        print(f"\nPrénom : {self.prenom}")
        print(f"Nom : {self.nom}")
        print(f"Numéro : {self.numero}")
        print(f"E-Mail : {self.email}")
        print(f"ID : {self.identifiant}")

    def ajouter(self, liste: list):
        print(f"\n--'{self.full_name()}' a été ajouté à la liste des contacts --")
        liste.append(self)

    def supprimer(self, liste: list):
        print(
            f"\n--'{self.nom.upper()} {self.prenom}' a été supprimé de la liste des contacts --"
        )
        liste.remove(self)
    
    def modifier_prenom(self):
        new_prenom = input("Prénom : ").capitalize()
        if verif_prenom_nom(new_prenom) == "erreur":
            return "erreur"
        self.prenom = new_prenom
        print("-- Modification effectuée --")

    def modifier_nom(self):
        new_nom = input("Nom : ").capitalize()
        if verif_prenom_nom(new_nom) == "erreur":
            return "erreur"
        self.nom = new_nom
        print("-- Modification effectuée --")

    def modifier_numero(self):
        new_numero = input("Numéro : ")
        if verif_numero(new_numero) == "erreur":
            return "erreur"
        self.numero = numero_formate(new_numero)
        print("-- Modification effectuée --")

    def modifier_email(self):
        new_email = input("E-mail : ")
        if verif_email(new_email) == "erreur":
            return "erreur"
        self.email = new_email
        print("-- Modification effectuée --")



def generate_id(liste_id: list):
    contact_id = f"{random.randint(0, 999999):06d}"
    while contact_id in liste_id:
        contact_id = f"{random.randint(0, 999999):06d}"
    liste_id.append(contact_id)
    return contact_id


def numero_formate(numero: str):
    resultat = ""
    for i in range(0, len(numero), 2):
        resultat += numero[i : i + 2] + " "
    return resultat.strip()


def menu():
    print("""
====== DATAMANAGER - CONTACTS ======

    1 - Ajouter un contact
    2 - Supprimer un contact
    3 - Modifier un contact
    4 - Rechercher un contact
    5 - Afficher tous les contacts
    6 - Supprimer tous les contacts
    7 - Quitter
""")


def navigation(liste: list, liste_id: list):
    num = input("|  Veuiller rentrer un chiffre ->  ")
    if num in ["1", "2", "3", "4", "5", "6", "7"]:
        if num == "1":
            ajouter_contact(liste, liste_id)
        elif num == "2":
            supprimer_contact(liste, liste_id)
        elif num == "3":
            modifier_contact(liste)
        elif num == "4":
            rechercher_contact(liste)
        elif num == "5":
            afficher_contacts(liste)
        elif num == "6":
            supprimer_tout(liste, liste_id)
        elif num == "7":
            return "quit"
    elif num == "":
        return
    else:
        print("\n-- ERREUR : Entrée invalide. Valides : '1', '2', '3', '4', '5', '6', '7' --")


def choisir_contact(liste: list):
    i = 1
    for contact in liste:
        print(f"{i} - {contact.full_name()}")
        i += 1
    try:
        choix = int(input("\nChoisissez un contact (numéro): "))
    except ValueError:
        print("\n-- ERREUR : Veuillez rentrez un numéro valide --")
        return "erreur"
    if 1 <= choix <= len(liste):
        return liste[choix - 1]
    else:
        print("\n-- ERREUR : Veuillez rentrez un numéro valide --")
        return "erreur"


def verif_infos(prenom: str, nom: str, numero: str, email: str):
    if prenom != "" and nom != "" and numero != "" and email != "":
        if verif_prenom_nom(prenom+nom) == "erreur":
            return "erreur"
        if verif_numero(numero) == "erreur":
            return "erreur"
        if verif_email(email) == "erreur":
            return "erreur"
    else:
        print("\n-- ERREUR : Entrée vide --")
        return "erreur"

def verif_prenom_nom(prenom_nom: str):
    numbers = "0123456789"
    for lettre in prenom_nom:
        if lettre in numbers:
            print(
                "\n-- ERREUR : Entrée contenant un chiffre dans le prénom ou le nom --"
            )
            return "erreur"
    if not prenom_nom.isalpha():
        print(
            "\n-- ERREUR le nom et le prénom doivent comporter uniquement des lettres"
        )
        return "erreur"

def verif_numero(numero: str):
    if not numero.isdigit():
        print("\n-- ERREUR : Le numéro doit comporter uniquement des chiffres --")
        return "erreur"
    if len(numero) != 10:
        print("\n-- ERREUR : Le numéro doit comporter dix chiffres --")
        return "erreur"

def verif_email(email: str):
    if "@" not in email or ".com" not in email:
        print("\n-- ERREUR : Adresse e-mail invalide --")
        return "erreur"

def ajouter_contact(liste: list, liste_id: list):
    print("\n--- AJOUT CONTACT ---")
    prenom = input("\nPrénom : ").capitalize().strip()
    nom = input("Nom : ").capitalize().strip()
    numero = input("Numéro : ")
    email = input("E-mail : ")
    identifiant = generate_id(liste_id)

    if verif_infos(prenom, nom, numero, email) != "erreur":
        numero = numero_formate(numero)
        new_contact = Contact(
            prenom,
            nom,
            numero,
            email,
            identifiant,
        )
        new_contact.ajouter(liste)


def supprimer_contact(liste: list, liste_id: list):
    if liste == []:
        print("\n-- Aucun contact dans la liste de contacts --")
        return
    print("\n--- SUPPRESSION CONTACT ---")
    contact = choisir_contact(liste)
    if contact == "erreur":
        return
    contact.supprimer(liste)
    liste_id.remove(contact.identifiant)


def afficher_contacts(liste: list):
    if liste == []:
        print("\n-- Aucun contact dans la liste de contacts --")
        return
    print("\n--- AFFICHAGE DES CONTACTS ---")
    for contact in liste:
        contact.afficher()


def rechercher_contact(liste: list):
    if liste == []:
        print("\n-- Aucun contact dans la liste de contacts --")
        return
    print("""\n
    --- RECHERCHE DE CONTACT ---

-> Types de recherche :
  1 - Par PRÉNOM ou NOM
  2 - Par NUMÉRO de téléphone
  3 - Par ADRESSE E-MAIL
  4 - Par ID
  5 - Retour au menu

""")


    liste_resultats = navigation_recherche(liste)
    if liste_resultats == "erreur":
        return
    print(f" - Résultat(s) : {len(liste_resultats)} contact(s) trouvé(s)\n")
    if liste_resultats == "quit":
        return
    if len(liste_resultats) == 0:
        return


    contact = choisir_contact(liste_resultats)
    if contact == "erreur":
        return
    contact.afficher()


def navigation_recherche(liste: list):
    print("- Veuillez chosir votre type de recherche")
    choix = input("   -> ")

    if choix == "1":
        recherche = input("Nom ou prénom : ").lower()
        liste_resultats = rechercher_nom_prenom(liste, recherche)
        return liste_resultats

    elif choix == "2":
        recherche = input("Numéro : ")
        liste_resultats = rechercher_numero(liste, recherche)
        return liste_resultats

    elif choix == "3":
        recherche = input("Email : ").lower()
        liste_resultats = rechercher_email(liste, recherche)
        return liste_resultats

    elif choix == "4":
        recherche = input("ID : ")
        liste_resultats = rechercher_id(liste, recherche)
        return liste_resultats
    
    elif choix == "5":
        return "quit"
    
    else:
        print("-- ERREUR : Choix invalide --")
        return "erreur"


def rechercher_nom_prenom(liste: list, recherche: str):
    if recherche == "":
        return []
    liste_resultats = []
    for contact in liste:
        initiale_prenom = (contact.prenom[0]).lower()
        initiale_nom = (contact.nom[0]).lower()
        initiale_match = recherche[0] == initiale_prenom or recherche[0] == initiale_nom
        if len(recherche) == 1 and initiale_match:
            liste_resultats.append(contact)
        elif initiale_match and (
            recherche in (contact.nom).lower() or recherche in (contact.prenom).lower()
        ):
            liste_resultats.append(contact)
    return liste_resultats


def rechercher_numero(liste: list, recherche: str):
    liste_resultats = []
    for contact in liste:
        numero = (contact.numero).replace(" ", "")
        if recherche.replace(" ", "") == numero:
            liste_resultats.append(contact)
    return liste_resultats

def rechercher_email(liste: list, recherche: str):
    if recherche == "":
        return []
    liste_resultats = []
    for contact in liste:
        initiale_match = recherche[0] == (contact.email[0]).lower()
        if initiale_match and recherche in (contact.email).lower():
            liste_resultats.append(contact)
    return liste_resultats

def rechercher_id(liste: list, recherche: str):
    liste_resultats = []
    for contact in liste:
        if recherche == contact.identifiant:
            liste_resultats.append(contact)
    return liste_resultats 


def supprimer_tout(liste: list, liste_id: list):
    if liste == []:
        print("\n-- Aucun contact dans la liste de contacts --")
        return
    valide = False
    while not valide :
        print("--- Êtes-vous sûr de vouloir supprimer tous les contact (o/n) ? ---")
        validation = input("   -> ")
        validation = validation.strip().lower()
        if validation == "o":
            print(f"-- Supression de {len(liste)} contact(s) effectuée --")
            liste.clear()
            liste_id.clear()
            valide = True

        elif validation == "n":
            print("-- Retour au menu --")
            valide = True

        else:
            print("-- ERREUR : Entrée invalide --")

def modifier_contact(liste: list):
    if liste == []:
        print("\n-- Aucun contact dans la liste de contacts --")
        return
    print("\n--- MODIFICATION DE CONTACT---")
    
    contact = choisir_contact(liste)
    if contact == "erreur":
        return
    contact.afficher()
    if navigation_modif(contact) == "quit":
        return
    

def navigation_modif(contact: Contact):
    print(f"\n--- Modification de '{contact.full_name()}' ---")
    print("""
    1 - Modifier le PRÉNOM
    2 - Modifier le NOM
    3 - Modifier le NUMÉRO
    4 - Modifier l'E-MAIL
    5 - Retour au menu
""")
    choix = input("   -> ")
    if choix == "1":
        contact.modifier_prenom()
    elif choix == "2":
        contact.modifier_nom()
    elif choix == "3":
        contact.modifier_numero()
    elif choix == "4":
        contact.modifier_email()
    elif choix == "5":
        return "quit"

def main():
    liste_id = []
    liste_contacts = []
    quitter = False
    while not quitter:
        menu()
        if navigation(liste_contacts, liste_id) == "quit":
            quitter = True


if __name__ == "__main__":
    main()
