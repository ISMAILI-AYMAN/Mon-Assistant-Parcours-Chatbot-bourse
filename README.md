# Mon-Assistant-Parcours-Chatbot-bourse
Ce projet propose une interface locale de chat pour interagir avec une base de données de connaissance. Le code implémente une application Streamlit qui permet aux utilisateurs d’interroger un chatbot capable de comprendre et de répondre à des questions  basées sur les bourses d'études. Il utilise les bibliothèques LangChain Community pour traiter et interroger le contenu des documents en s'appuyant sur un magasin vectoriel et des modèles locaux d'ollama ("mxbai-embed-large:latest" et "Mistral"). L'application est conçue pour une utilisation locale.
# Les dépendances 
- **LangChain Community** : Pour le stockage vectoriel, les modèles de chat, les embeddings et le chargement de documents.
- **Streamlit** : Pour créer l’interface de l’application web.
- **Ollama Mistral** : Le modèle de langage utilisé pour générer les réponses.
- **mxbai-embed-large:latest** : le modèle utilisé pour faire les embeddings

# Installation
Pour configurer l’environnement et exécuter ce projet, suivez les étapes ci-dessous :
1. Clôner le dépôt ou le télécharger
```bash 
git clone https://github.com/i038615/local_rag/
cd [repository-directory]
```
2. Installer les dépendances : 
 Assurez-vous que Python 3.10+ est installé, puis exécutez :
 ```bash
 pip install -r requirements.txt
 ```
3. Télécharger les modèles : Ce projet utilise les modèle Ollama Mistral et mxbai-embed-large:latest . Suivez la documentation officielle d’Ollama pour installer les modèles pour une utilisation locale.
</details>

# Fonctionnement
- **ingest.py** : Charge les documents PDF d'un dossier, les découpe en morceaux gérables, et indexe ces morceaux dans un magasin vectoriel pour une récupération efficace.
- **Local_rag.py** : Configure le mécanisme de recherche qui permet d’interroger le magasin vectoriel pour trouver les morceaux pertinents d’un document.Traite une requête en récupérant le contexte pertinent à partir du magasin vectoriel et en le passant, avec la requête, au modèle de chat pour générer une réponse.

# Contribution
Les contributions à ce projet sont les bienvenues.

# Auteurs 
**AKAKPO Koffi Moïse**
**ISMAILI Ayman**



