from langchain_google_genai import ChatGoogleGenerativeAI



def ask_question( context= ""):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    result = llm.invoke(context)

    return result