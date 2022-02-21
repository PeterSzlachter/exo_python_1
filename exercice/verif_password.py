mdp = input("Entez un mot de passe minimun 8 caractères (nombre et lettres) : ")
mdp_trop_court = "votre mot de passe est trop court"
mdp_nombre = "votre mot de passe ne contient que des nombres"
mdp_sucess = "inscription terminée"

if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif len(mdp) < 8 :
    print(mdp_trop_court.capitalize())

elif mdp.isdigit():
    print(mdp_nombre.capitalize())
else:
    print(mdp_sucess.capitalize())