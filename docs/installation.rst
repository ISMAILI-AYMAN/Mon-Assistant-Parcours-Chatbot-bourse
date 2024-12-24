================
INSTALLATION
================
----------------
Les dépendances 
----------------
- **LangChain Community** : Pour le stockage vectoriel, les modèles de chat, les embeddings et le chargement de documents.

- **Streamlit** : Pour créer l’interface de l’application web.

- **Ollama Mistral** : Le modèle de langage utilisé pour générer les réponses.

- **mxbai-embed-large:latest** : le modèle utilisé pour faire les embeddings.

-------------
Installation
-------------
Pour configurer l’environnement et exécuter ce projet, suivez les étapes ci-dessous :

1. Clôner le dépôt ou le télécharger

```bash 
git clone https://github.com/i038615/local_rag/
cd [repository-directory]
```
2. Installer les dépendances : 

 Assurez-vous que Python 3.10(de préférence) est installé, puis exécutez :
 ```bash
 pip install -r requirements.txt
 ```
3. Télécharger les modèles : Ce projet utilise les modèle Ollama Mistral et mxbai-embed-large:latest . Suivez la documentation officielle d’Ollama pour installer les modèles pour une utilisation locale.
4. Création des dossiers documents et data:

   Le dossier "documents" contient tous les fichiers pdf à utiliser

   Le dossier "data" sert à stocker la base de données chroma


