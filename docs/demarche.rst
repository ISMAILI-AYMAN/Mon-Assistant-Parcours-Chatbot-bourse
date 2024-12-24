=============================================
DEMARCHE SUIVI POUR LA REALISATION DU PROJET
=============================================

--------------------------------
1. Elaboration du plan de projet
--------------------------------
Afin de mener à bien ce projet, nous avons décidé d'utiliser l'approche RAG (Retrieval-Augmented Generation).

.. image:: https://opendatascience.com/wp-content/uploads/2024/02/va4.png
   :alt: Principe du RAG
   :width: 400px
   :align: center

Le principe de cette approche est d'établir une base de données Chroma qui va servir de connaissance au chatbot. 
Pour ce faire, nous avons décidé de créer deux fichiers Python. L'un va servir à l'obtention de la base de données et 
l'autre va servir à la récupération et à l'interface Streamlit.

En ce qui concerne l'interface Streamlit, nous avons opté pour une interface simpliste.

----------------------------
2. Développement du chatbot
----------------------------
Structure du projet :

1. **Fichiers** :

   - `ingest.py` : permet d'obtenir le vectorstore Chroma.
   - `Local_rag.py` : permet de lancer l'application et gérer l'interface utilisateur.

2. **Dossiers** :

   - "documents" : contient les fichiers PDF des bourses d'études.
   - "data" : stocke le vectorstore Chroma.

.. image:: https://drive.google.com/file/d/1DfwADJKu5az-cGOhEr3Us3hmPOYPMVys/view?usp=drive_link
   :alt: Développement
   :width: 400px
   :align: center

