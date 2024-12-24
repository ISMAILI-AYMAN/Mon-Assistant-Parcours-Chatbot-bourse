=============================================
DEMARCHE SUIVI POUR LA REALISATION DU PROJET
=============================================

--------------------------------
1. Elaboration du plan de projet
--------------------------------
Afin de mener à bien ce projet, nous avons décider d'utiliser l'approche RAG(Retrivial Augmentation Generation).\ 
.. image:: https://opendatascience.com/wp-content/uploads/2024/02/va4.png
   :alt: Principe du RAG
   :width: 400px
   :align: center

Le principe de cet approche est d'établir une base de données Chroma qui va servir de connaissance au chatbot. 
Pour se faire, nous avons décidé de créer deux fichiers python. L'un va servir à l'obtention de la base de donnée et 
l'autre va servir à la récupération et l'interface streamlit.
En ce qui concerne l'interface streamlit, nous avons opté pour une interface simpliste.

----------------------------
2. Développement du chatbot
----------------------------
Les fichiers python : 
- Dossier "documents": contient les fichiers pdfs de bourse d'étude
- Dossier "data" : permet de stocker le vectorstore chroma
- ingest.py : permet d'obtenir le vectorstore chroma
- Local_rag.py : permet de faire la récupération et le lancement de l'application
