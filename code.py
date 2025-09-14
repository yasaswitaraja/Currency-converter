import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt
from docx import Document
import io
from wordcloud import WordCloud



def extract_text_from_word(iobytes):
    doc = Document(io.BytesIO(iobytes))
    paras=[]
    for para in doc.paragraphs:
        paras.append(para.text)
    return ' '.join(paras)

def extract_text_from_pdf(iobytes):
    doc = pdfplumber.open(io.BytesIO(iobytes))
    pages=[]
    for page in doc.pages:
        pages.append(page.extract_text())
    return ' '.join(pages)


def wordcloud(uploaded):  
    iobytes = uploaded.read()
    if uploaded.name.lower().endswith('pdf'):
        text = extract_text_from_pdf(iobytes)
        image=WordCloud().generate(text)
        fig,ax=plt.subplots(figsize=(10,7))
        ax.imshow(image)
        ax.axis('off')
        st.pyplot(fig)
    else:
        text = extract_text_from_word(iobytes)
        image=WordCloud().generate(text)
        fig,ax=plt.subplots(figsize=(10,7))
        ax.imshow(image)
        ax.axis('off')
        st.pyplot(fig)


         
        
    




st.set_page_config(layout='centered')
st.title('Word Cloud from PDF or Word')
uploaded = st.file_uploader('Upload any PDF or WORD')
if uploaded:
    wordcloud(uploaded)





