from langchain_core.prompts import ChatPromptTemplate
import pypdf

def create_prompt():
    template = """
    You are a chatbot that answers questions based on a provided PDF document.
    
    PDF Content: {pdf_text}

    User Question: {question}

    Answer:
    """
    return ChatPromptTemplate.from_template(template)

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = pypdf.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text
