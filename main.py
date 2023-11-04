import DS
import art
import colorama

print(colorama.Fore.RED)
print(art.text2art("MP2-Cyber"))
print(art.text2art("DS:PYTHON"))
print(art.text2art("PROF SOUHAIB"))
print(colorama.Fore.MAGENTA)
if __name__ == "__main__":

    print("bienvenu dans l'application")
    print("1/ pour authentification")
    print("2/ pour enregistrement")
    choix = input("1 ou 2  ")
    if choix == "1" :
            email = DS.Introduire_email()
            p_hashed = DS.Introduire_pwd()
            with open("cyber.txt", "r") as file:
                 cyber = file.read()
            if f"Email: {email}\n" in cyber and f"Pwd: {p_hashed}\n" in cyber:
                 DS.Menu()
            else:
                 print("veillez vous enregistrer")
                 DS.enregistrer_utilisateur()
    else:
            choix == "2"
            DS.enregistrer_utilisateur()
