import csv
import os

# Nom du fichier pour stocker les contacts
FICHIER_CONTACTS = 'contacts.csv'

# Fonction pour vérifier si le fichier existe, sinon le créer
def initialiser_fichier():
    if not os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Téléphone"])  # Entêtes de colonne

# Fonction pour ajouter un contact
def ajouter_contact(nom, telephone):
    with open(FICHIER_CONTACTS, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nom, telephone])
    print(f"Contact {nom} ajouté avec succès.")

# Fonction pour afficher tous les contacts
def afficher_contacts():
    with open(FICHIER_CONTACTS, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Sauter la première ligne (entête)
        contacts = list(reader)

        if len(contacts) == 0:
            print("Aucun contact enregistré.")
        else:
            print("Liste des contacts :")
            for contact in contacts:
                print(f"Nom: {contact[0]}, Téléphone: {contact[1]}")

# Fonction pour supprimer un contact par nom
def supprimer_contact(nom):
    contacts_mis_a_jour = []
    contact_trouve = False
    
    with open(FICHIER_CONTACTS, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        entetes = next(reader)
        for contact in reader:
            if contact[0] != nom:
                contacts_mis_a_jour.append(contact)
            else:
                contact_trouve = True
    
    if contact_trouve:
        with open(FICHIER_CONTACTS, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(entetes)
            writer.writerows(contacts_mis_a_jour)
        print(f"Le contact {nom} a été supprimé.")
    else:
        print(f"Aucun contact trouvé avec le nom {nom}.")

# Fonction pour afficher le menu
def afficher_menu():
    print("\nGestionnaire de Contacts")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Supprimer un contact")
    print("4. Quitter")

# Fonction principale
def main():
    initialiser_fichier()

    while True:
        afficher_menu()
        choix = input("\nSélectionnez une option (1-4) : ")
        
        if choix == '1':
            nom = input("Entrez le nom du contact : ")
            telephone = input("Entrez le numéro de téléphone : ")
            ajouter_contact(nom, telephone)
        
        elif choix == '2':
            afficher_contacts()
        
        elif choix == '3':
            nom = input("Entrez le nom du contact à supprimer : ")
            supprimer_contact(nom)
        
        elif choix == '4':
            print("Merci d'avoir utilisé le gestionnaire de contacts !")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()
