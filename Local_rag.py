import streamlit as st
from streamlit_chat import message
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from ingest import main

# Initialisation de la base de données
if "db" not in st.session_state:
    # Initialise la base de données une seule fois
    st.session_state.db = main()  

# Fonction pour récupérer des réponses depuis la base de données
def retrieve_from_db(question):
    model = ChatOllama(model="mistral")
    retriever = st.session_state.db.similarity_search(question, k=5)

    after_rag_template = """Tu es un assistant spécialisé dans les parcours de bourses d'études. Ton rôle est d'aider les utilisateurs à trouver les opportunités de bourses les plus adaptées à leur profil, tout en agissant comme un conseiller et un guide personnalisé.
    Tu ne réponds qu'en français.

    Voici tes responsabilités principales :
    1. **Réponses basées sur le contexte** : Si une question concerne une bourse présente dans la base de données fournie (le contexte), donne une réponse claire et détaillée basée uniquement sur ces informations.
    2. **Propositions adaptées** : Si l'utilisateur n'a pas donné assez d'informations sur son profil (par exemple, pays d'origine, niveau d'études, domaine d'intérêt, etc.), invite-le poliment à fournir ces détails pour mieux l'aider.
    3. **Suggestions de bourses** : Une fois que tu as suffisamment d'informations sur l'utilisateur, propose des opportunités de bourses pertinentes et justifie pourquoi elles conviennent à son profil.
    4. **Guidance proactive** : Si une réponse n'est pas disponible dans la base de données, informe l'utilisateur de manière honnête et propose des pistes ou questions complémentaires pour clarifier ses besoins ou explorer d'autres options.

    Lorsque tu formules tes réponses :
    - Sois bienveillant, clair et informatif.
    - Agis comme un mentor qui cherche à maximiser les chances de l'utilisateur de trouver une bourse adaptée.

    Exemple de réponse si aucune information pertinente n'est trouvée dans la base :
    "Je suis désolé, mais je n'ai pas cette réponse dans mes données actuelles. Cependant, pourriez-vous préciser votre niveau d'études, votre domaine d'intérêt ou le pays où vous recherchez une bourse ? Cela m'aidera à vous orienter davantage."

    Tu as accès à la base de données suivante contenant des informations sur les bourses d'études :
    {context}

    Question : {question}"""

    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)

    after_rag_chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | after_rag_prompt
        | model
        | StrOutputParser()
    )

    return after_rag_chain.invoke({"context": retriever, "question": question})


# Configuration de l'application Streamlit
st.set_page_config(page_title="💬 Mon Assistant Parcours de bourses d'études", layout="wide")

# Thème sombre et style des messages
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;
        color: white;
    }
    .stButton>button {
        background-color: #2C2C2C;
        color: white;
        border: 1px solid #3E3E3E;
    }
    .stTextInput>div>div>input {
        background-color: #2C2C2C;
        color: white;
    }
    .stTextInput>div>label {
        color: white;
    }
    .message-box {
        display: flex;
        align-items: center;
        margin: 10px 0;
    }
    .user-message {
        background-color: #0078D4;
        color: white;
        padding: 10px;
        border-radius: 10px;
        max-width: 60%;
        text-align: left;
    }
    .bot-message {
        background-color: #444444;
        color: white;
        padding: 10px;
        border-radius: 10px;
        max-width: 60%;
        text-align: left;
    }
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
    }
    .user-container {
        justify-content: flex-end;
    }
    .bot-container {
        justify-content: flex-start;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titre de l'application
st.title("💬 Mon Assistant Parcours")
st.sidebar.title("Description & Fonctionnalités")
st.sidebar.text("Ce chatbot est conçu pour répondre à vos questions sur les bourses d'études!")

# Initialisation de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
st.write("Chat")
for msg in st.session_state.messages:
    if msg["user"] == "user":
        st.markdown(
            f"""
            <div class="message-box user-container">
                <div class="user-message">{msg['content']}</div>
                <img class="avatar" src="https://via.placeholder.com/40/0078D4/FFFFFF/?text=U">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="message-box bot-container">
                <img class="avatar" src="https://via.placeholder.com/40/444444/FFFFFF/?text=B">
                <div class="bot-message">{msg['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Entrée utilisateur
question = st.text_input("Posez votre question ici :", "")

# Gestion de la logique des réponses
if st.button("Envoyer"):
    if question:
        # Ajout de la question à l'historique
        st.session_state.messages.append({"user": "user", "content": question})
        
        # Génération de la réponse
        answer = retrieve_from_db(question)
        
        # Ajout de la réponse à l'historique
        st.session_state.messages.append({"user": "bot", "content": answer})

        # Réinitialisation de la question
        question = ""
        
