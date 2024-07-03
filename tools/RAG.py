
from langchain_community.document_loaders import PyPDFLoader
import numpy as np
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from huggingface_hub import login
from langchain_community.llms import HuggingFaceHub






def pdf_loader(file_path):
        
    loader = PyPDFLoader(file_path)

    docs = loader.load()

    print(len(docs))
    #print(docs[0].page_content[0:100])
    #print(docs[0].metadata)

    return docs

def splitting(docs):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 700,
    chunk_overlap  = 50,
    )
    docs_after_split = text_splitter.split_documents(docs)

    #print(docs_after_split[0])
    
    return docs_after_split



def print_avg_values(docs,docs_after_split):
    avg_doc_length = lambda docs: sum([len(doc.page_content) for doc in docs])//len(docs)
    avg_char_before_split = avg_doc_length(docs)
    avg_char_after_split = avg_doc_length(docs_after_split)

    print(f'Before split, there were {len(docs)} documents loaded, with average characters equal to {avg_char_before_split}.')
    print(f'After split, there were {len(docs_after_split)} documents (chunks), with average characters equal to {avg_char_after_split} (average chunk length).')

        
    return None



def load_embedding():
    
    
    huggingface_embeddings = HuggingFaceBgeEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",  # alternatively use "sentence-transformers/all-MiniLM-l6-v2" for a light and faster experience.
        model_kwargs={'device':'cpu'}, 
        encode_kwargs={'normalize_embeddings': True}
    )
    return    huggingface_embeddings 

def sample_embedding(huggingface_embeddings,docs_after_split):
    sample_embedding = np.array(huggingface_embeddings.embed_query(docs_after_split[0].page_content))
    #print("Sample embedding of a document chunk: ", sample_embedding)
    print("Size of the embedding: ", sample_embedding.shape)

    return None

def load_vectorstore(docs_after_split,huggingface_embeddings):
    vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)
    print("vector store loaded \n")
    return vectorstore

def vector_store_query(vectorstore , query):
    
    relevant_documents = vectorstore.similarity_search(query)
    print(f'There are {len(relevant_documents)} documents retrieved which are relevant to the query. Display the first one:\n')
    print(relevant_documents[0].page_content)
    
    return None

def load_retirever(vectorstore):
    
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    print("retriever loaded \n")
    return retriever

def load_llm(HUGGINGFACEHUB_API_TOKEN):
    hf = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-v0.1",
    model_kwargs={"temperature": 0.1, "max_length": 500},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    llm = hf
    print("llm loaded \n")
    return llm



def get_prompt():
    prompt_template = """Use the following pieces of context to answer the question at the end. Please follow the following rules:
    1. If you don't know the answer, don't try to make up an answer. Just say "I can't find the final answer but you may want to check the following links".
    2. If you find the answer, write the answer in a concise way with five sentences maximum.

    {context}

    Question: {question}

    Helpful_Answer:
    """

    PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
    )

    return PROMPT
def load_retrievalQA(llm , retriever , PROMPT):
    
    retrievalQA = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
    )          
    print("retrievalQA loaded")
    return retrievalQA



def invoking_query_to_RAG(retrievalQA , query):
    
    result = retrievalQA.invoke({"query": query})
    print("\nresult",result['result'],"\n")


    relevant_docs = result['source_documents']
    print(f'There are {len(relevant_docs)} documents retrieved which are relevant to the query.')
    print("*" * 100)
    for i, doc in enumerate(relevant_docs):
        print(f"Relevant Document #{i+1}:\nSource file: {doc.metadata['source']}, Page: {doc.metadata['page']}\nContent: {doc.page_content}")
        print("-"*100)
        print(f'There are {len(relevant_docs)} documents retrieved which are relevant to the query.')
        
        
    
    return result


def words_after_target(result, target_word):
    sentence = result['result']
    words = sentence.split()  # Split the sentence into words
    if target_word in words:
        target_index = words.index(target_word)  # Find the index of the target word
        words_after = words[target_index + 1:]  # Get all words after the target word
       
        #print(" ".join(words_after))
        # Join and print the words after the target word
        words_after = " ".join(words_after)
        return words_after 

    else:
        print(f"The word '{target_word}' is not in the sentence.")
        return words
    
def RAG_output(query):
    login(token="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")
    HUGGINGFACEHUB_API_TOKEN = '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'


    '''query = """what would be the grade and stage on the basis of following prompt : the symptoms shown by the patient are large lesion on the top of my tongue . severe pain and tenderness . lot of difficulty chewing and speaking . hoarseness in my voice.
    duration and progresion of cancer are over 3 months. the conditions worsened overtime rapidly.
    Bleeding or Swellings are there is bleeding and swelling on the tongue.
    Lifestyle and Habits are heavy smoker for over 10 years. no history of HPV. 
    Medical and Family History are no such history or family history.
    Oral Hygiene and Dental History are  infrequent visit to dentist.
    Lesion Descriptions are the lesion is on the tongue. it is larger then 4 cm . it has a rough texture .the colour has darkened.
    Lymph Node Involvements are swelling below the jaw around 3 to 4 cm.
    Biopsy and Pathology Reports are no prior biopsy or imaging test.
    General Health and Functional Impacts are i am sick most of the time.
    Impacts on Daily Life are i feel tired and i have lost my apetite.
    Treatment History and Responses are no such treatments.
    overall health is no such illnessthe grade is predicted from the model is grade 3 and the stage stage 3." """  
    '''

    file_path = "src\pdfs\qna.pdf"
    target_word = "Classification:"
            
    docs = pdf_loader(file_path)
        

    docs_after_split = splitting(docs)

    print_avg_values(docs,docs_after_split)



    huggingface_embeddings = load_embedding()


    sample_embedding(huggingface_embeddings,docs_after_split)

    vectorstore =  load_vectorstore(docs_after_split,huggingface_embeddings)

    vector_store_query(vectorstore , query)


    retriever = load_retirever(vectorstore) # change search type and search kwargs in the function



    llm = load_llm(HUGGINGFACEHUB_API_TOKEN)  # change temperature , max length , repo_id in the function

    PROMPT = get_prompt()


    retrievalQA = load_retrievalQA(llm , retriever , PROMPT)

    print("\nquery : ",query,"\n")
    result1 = invoking_query_to_RAG(retrievalQA , query)
        
        
    answer = words_after_target(result1, target_word)

    cancer = answer[:33]
    print("\ncancer: ",cancer,"\n")

    treatment_query= f"\nhow can {cancer} be treated  \n"
    print(treatment_query)


    result2 = invoking_query_to_RAG(retrievalQA , treatment_query)

    final_answer = words_after_target(result2, "Helpful_Answer:")

    print("\nfinal answer : ",final_answer)

        
    return cancer,final_answer





def RAG_output_treatment(query):
    login(token="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")
    HUGGINGFACEHUB_API_TOKEN = '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'


    '''query = """what would be the grade and stage on the basis of following prompt : the symptoms shown by the patient are large lesion on the top of my tongue . severe pain and tenderness . lot of difficulty chewing and speaking . hoarseness in my voice.
    duration and progresion of cancer are over 3 months. the conditions worsened overtime rapidly.
    Bleeding or Swellings are there is bleeding and swelling on the tongue.
    Lifestyle and Habits are heavy smoker for over 10 years. no history of HPV. 
    Medical and Family History are no such history or family history.
    Oral Hygiene and Dental History are  infrequent visit to dentist.
    Lesion Descriptions are the lesion is on the tongue. it is larger then 4 cm . it has a rough texture .the colour has darkened.
    Lymph Node Involvements are swelling below the jaw around 3 to 4 cm.
    Biopsy and Pathology Reports are no prior biopsy or imaging test.
    General Health and Functional Impacts are i am sick most of the time.
    Impacts on Daily Life are i feel tired and i have lost my apetite.
    Treatment History and Responses are no such treatments.
    overall health is no such illnessthe grade is predicted from the model is grade 3 and the stage stage 3." """  
    '''

    #file_path = "src\pdfs\qna.pdf"
    file_path = "src/pdfs/treatment.pdf"
    target_word = "Classification:"
            
    docs = pdf_loader(file_path)
        

    docs_after_split = splitting(docs)

    print_avg_values(docs,docs_after_split)



    huggingface_embeddings = load_embedding()


    sample_embedding(huggingface_embeddings,docs_after_split)

    vectorstore =  load_vectorstore(docs_after_split,huggingface_embeddings)

    vector_store_query(vectorstore , query)


    retriever = load_retirever(vectorstore) # change search type and search kwargs in the function



    llm = load_llm(HUGGINGFACEHUB_API_TOKEN)  # change temperature , max length , repo_id in the function

    PROMPT = get_prompt()


    retrievalQA = load_retrievalQA(llm , retriever , PROMPT)

    print("\nquery : ",query,"\n")
    result = invoking_query_to_RAG(retrievalQA , query)
        
    
    final_answer   = words_after_target(result, "Helpful_Answer:")

    print("\nfinal answer : ",final_answer)

        
    return result , final_answer

if __name__=="__main__":
    query1 = """what would be the teatment when grade is 3 ." """  
    query2 = """what would be the teatment when stage is 3 . """
    result1,final_answer1 = RAG_output_treatment(query1)
    print("\nresult1 : ",result1)
    print("\nfinal_answer1 : ",final_answer1)
    result2,final_answer2 = RAG_output_treatment(query2)
    print("\nresult2 : ",result2)
    print("\nfinal_answer2 : ",final_answer2)


