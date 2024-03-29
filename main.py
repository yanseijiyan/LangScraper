import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


from langchain_openai import ChatOpenAI  # Certifique-se de importar corretamente
from langchain.chains import LLMChain, MapReduceDocumentsChain, ReduceDocumentsChain, StuffDocumentsChain
from langchain.prompts import PromptTemplate  # Verifique o caminho correto de importação
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()
OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")



class Document:
    def __init__(self, content, metadata=None):
        self.page_content = content
        # Inicializa metadata como um dicionário vazio se nenhum for fornecido
        self.metadata = metadata if metadata is not None else {}

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return Document(content, {'url': url})
    except requests.RequestException as e:
        return None


def process_documents(docs):
    llm = ChatOpenAI(temperature=0)


    # Map
    map_template = """The following is a set of documents
    {docs}
    Based on this list of docs, please identify the main themes 
    Helpful Answer:"""
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)



    # Reduce
    reduce_template = """The following is set of summaries:
    {docs}
    Take these and distill it into a final, consolidated summary of the main themes. 
    Helpful Answer:"""
    reduce_prompt = PromptTemplate.from_template(reduce_template)


    # Run chain
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

    # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain, document_variable_name="docs"
    )

    # Combines and iteratively reduces the mapped documents
    reduce_documents_chain = ReduceDocumentsChain(
        # This is final chain that is called.
        combine_documents_chain=combine_documents_chain,
        # If documents exceed context for `StuffDocumentsChain`
        collapse_documents_chain=combine_documents_chain,
        # The maximum number of tokens to group documents into.
        token_max=4000,
    )

    # Combining documents by mapping a chain over them, then combining results
    map_reduce_chain = MapReduceDocumentsChain(
        # Map chain
        llm_chain=map_chain,
        # Reduce chain
        reduce_documents_chain=reduce_documents_chain,
        # The variable name in the llm_chain to put the documents in
        document_variable_name="docs",
        # Return the results of the map steps in the output
        return_intermediate_steps=False,
    )

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=0
    )
    split_docs = text_splitter.split_documents(docs)
    
    return map_reduce_chain.invoke(split_docs)




