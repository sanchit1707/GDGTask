from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

def analytical_chatbot(question:str)-> str:
    embeddings=HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    news_db=FAISS.load_local(
        "vectorstores/news_store",embeddings,
        allow_dangerous_deserialization=True 
    )
    docs=news_db.similarity_search(question,k=4)
    context="\n".join(d.page_content for d in docs)

    prompt=f"""
you are professional financial assistant. 
Relevant News:{context}
Question:{question}

RULES:
- Explain WHY the market behaves this way
- Use news as evidence
- Do NOT predict prices
- Do NOT give buy/sell advice
"""
    return llm.invoke(prompt).content