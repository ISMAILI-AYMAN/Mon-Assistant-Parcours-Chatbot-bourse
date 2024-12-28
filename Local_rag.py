import streamlit as st
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from ingest import main

# Initialisation de la base de données
if "db" not in st.session_state:
    st.session_state.db = main()  

# Initialisation de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Fonction pour récupérer des réponses depuis la base de données
def retrieve_from_db(question):
    model = ChatOllama(model="mistral")
    retriever = st.session_state.db.similarity_search(question, k=5)

    after_rag_template = """Tu es un assistant spécialisé dans les parcours de bourses d'études. Ton rôle est d'aider les utilisateurs à trouver les opportunités de bourses les plus adaptées à leur profil. 
    Tout en agissant comme un conseiller et un guide personnalisé. Tu ne réponds qu'en français.
    Contexte : {context}
    Question : {question}"""

    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)

    after_rag_chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | after_rag_prompt
        | model
        | StrOutputParser()
    )

    return after_rag_chain.invoke({"context": retriever, "question": question})


# Configuration de la page Streamlit
st.set_page_config(page_title="🎓 Assistant Bourses d'Études", layout="wide")

# Sidebar pour l'historique des questions
st.sidebar.title("💬 Historique des Questions")
if st.session_state.messages:
    for i, msg in enumerate(st.session_state.messages):
        if msg["user"] == "user":
            st.sidebar.write(f"🔹 {i+1}. {msg['content']}")

# Titre principal
st.title("🎓 Assistant Parcours de Bourses d'Études")

# Affichage des messages
st.write("**Discussion**")
for msg in st.session_state.messages:
    if msg["user"] == "user":
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
                <div style="background-color: #0078D4; color: white; padding: 10px; border-radius: 10px; max-width: 60%; text-align: left;">
                    {msg['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-start; margin-bottom: 10px;">
                <div style="background-color: #444444; color: white; padding: 10px; border-radius: 10px; max-width: 60%; text-align: left;">
                    {msg['content']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Zone de saisie utilisateur avec possibilité d'aller à la ligne
question = st.text_area("Posez votre question ici :", "", height=100, placeholder="Tapez votre question...")

# Bouton d'envoi avec une icône de flèche
send_button = st.button("Envoyer ", use_container_width=True)

# Gestion des réponses
if send_button and question.strip():
    # Ajout de la question à l'historique
    st.session_state.messages.append({"user": "user", "content": question.strip()})
    
    # Génération de la réponse
    with st.spinner("L'Assistant rédige sa réponse..."):
        try:
            answer = retrieve_from_db(question.strip())
        except Exception as e:
            answer = "Je suis désolé, une erreur est survenue. Veuillez réessayer plus tard."
    
    # Ajout de la réponse à l'historique
    st.session_state.messages.append({"user": "bot", "content": answer})
    
    # Efface la zone de saisie
    st.text_area("Posez votre question ici :", "", key="question", height=100)
