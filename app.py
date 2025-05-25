import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

import pandas as pd

users = pd.read_csv('./users.csv')

data = {'usernames':{}}
for i, user in users.iterrows():
    data['usernames'][user['name']]={
        'name': user['name'],
        'password': user['password'],
        'email': user['email'],
        'failed_login_attemps': user['failed_login_attemps'],  # Sera géré automatiquement
        'logged_in': user['logged_in'],          # Sera géré automatiquement
        'role': user['role']
    }

def tips_connexion():
    if st.checkbox('show tips?'):
        with st.sidebar:
            st.subheader('Exemples pour se connecter')
            user_ex=[]
            for x in data['usernames'].values():
                user_ex.append({
                    'user':x['name'],
                    'mdp':x['password']
                })
            st.dataframe(user_ex)


# data['usernames'] = users.to_dict(orient='index')
# Nos données utilisateurs doivent respecter ce format
# lesDonneesDesComptes = {
#     'usernames': {
#         'utilisateur': {
#             'name': 'utilisateur',
#             'password': 'utilisateurMDP',
#             'email': 'utilisateur@gmail.com',
#             'failed_login_attemps': 0,  # Sera géré automatiquement
#             'logged_in': False,          # Sera géré automatiquement
#             'role': 'utilisateur'
#         },
#         'root': {
#             'name': 'root',
#             'password': 'rootMDP',
#             'email': 'admin@gmail.com',
#             'failed_login_attemps': 0,  # Sera géré automatiquement
#             'logged_in': False,          # Sera géré automatiquement
#             'role': 'administrateur'
#         }
#     }
# }

if st.session_state['name'] == None:
    tips_connexion()

authenticator = Authenticate(
    data,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)


authenticator.login()



def accueil():
    st.title("Bienvenu sur sur ta page d'accueil")

def photos():
    st.title('Bienvenu dans ton album photo')
    
    # Création de 3 colonnes
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne : 
    with col1:
        st.subheader("Le chat potté")
        st.image("./images/chatpotte.jpg")

    # Contenu de la deuxième colonne :
    with col2:
        st.subheader("Double face")
        st.image("./images/doubleface.jpg")

    # Contenu de la troisième colonne : 
    with col3:
        st.subheader("Une chatte célèbre")
        st.image("./images/catwoman.jpg")
  




if st.session_state["authentication_status"]:
    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        st.write(f'Bienvenu {st.session_state['name']}!  \nContent de te revoir')
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

    if selection == 'Accueil':
        accueil()

    elif selection == 'Photos':
        photos()

    

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')