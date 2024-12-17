import imaplib
import email
from email.header import decode_header
import webbrowser
import pyperclip
import re
import time
import keyboard  # Bibliothèque pour détecter les touches
from datetime import datetime, timedelta
from langdetect import detect

# Configuration de l'email
IMAP_SERVER = "imap.gmail.com"
EMAIL = "your_email@gmail.com"  # Remplace par ton email
PASSWORD = "your_app_password"  # Mot de passe d'application

# Fonction pour se connecter à la boîte email
def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    return mail

# Fonction pour chercher le dernier lien de confirmation dans les emails reçus dans les 10 dernières minutes
def get_confirmation_link_and_code(mail):
    # Sélectionner la boîte de réception
    mail.select("inbox")

    # Chercher les emails reçus dans les 10 dernières minutes
    since_time = (datetime.now() - timedelta(minutes=10)).strftime("%d-%b-%Y")
    status, messages = mail.search(None, f'(SINCE {since_time})')
    email_ids = messages[0].split()
    
    if not email_ids:
        return None, None

    # Parcourir les emails récents
    for email_id in reversed(email_ids):
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Décoder le message
                msg = email.message_from_bytes(response_part[1])
                
                # Obtenir le contenu de l'email
                body = None
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                
                # Chercher un lien (exemple : lien de confirmation HTTP/HTTPS)
                link = None
                if body:
                    match_link = re.search(r"https?://[^\s]+", body)
                    if match_link:
                        link = match_link.group(0)

                    # Chercher un code (exemple : 6 chiffres)
                    match_code = re.search(r"\b\d{6}\b", body)
                    if match_code:
                        code = match_code.group(0)
                    else:
                        code = None
                    
                    return link, code
    return None, None

# Fonction principale
def main():
    print("Connexion au serveur IMAP...")
    mail = connect_to_email()
    print("Connecté. Attente de la combinaison 'Ctrl + ''' pour vérifier les emails...")
    
    try:
        while True:
            # Attendre que l'utilisateur appuie sur 'Ctrl + '''
            if keyboard.is_pressed('ctrl+\''):  # Vérifie si 'Ctrl + ' est pressé
                print("Commande détectée. Vérification des emails...")

                # Rechercher le lien de confirmation et le code
                link, code = get_confirmation_link_and_code(mail)
                
                if link:
                    print(f"Lien trouvé : {link}")
                    print("Ouverture du lien dans le navigateur...")
                    webbrowser.open(link)  # Ouvre le lien dans le navigateur par défaut
                
                if code:
                    pyperclip.copy(code)  # Copie le code dans le presse-papier
                    print(f"Code copié dans le presse-papier : {code}")
                
                if not link and not code:
                    print("Aucun nouvel email avec lien ou code trouvé.")
                
                # Attendre un peu avant de recommencer pour éviter un surmenage CPU
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\nDéconnexion.")
        mail.logout()

# Lancer le script
if __name__ == "__main__":
    main()

