import streamlit as st
import pdf2image
from PIL import Image
import pytesseract
from pytesseract import Output, TesseractError
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF, images_to_txt

st.title("🎈 My new app")

languages = {
    'English': 'eng',
    'Indonesia': 'ind',
}

with st.sidebar:
    st.title(":outbox_tray: LOREM IPSUM")

    st.markdown("""
    # How does it work?
    LOREM IPSUM
    """)
    
    st.markdown("""
    Made by LOREM IPSUM
    """)
    st.markdown("""
    Reference Credits [@nainia_ayoub](https://github.com/nainiayoub/pdf-text-data-extractor) 
    """)
    

pdf_file = st.file_uploader("Load your PDF", type=['pdf'])

if pdf_file:
    path = pdf_file.read()
    file_extension = pdf_file.name.split(".")[-1]
    
    # display document
    with st.expander("Display document"):
        displayPDF(path)

    option = st.selectbox('Select the document language', list(languages.keys()))
    
    # Convert PDF to Text
    texts, nbPages = images_to_txt(path, languages[option])
    totalPages = "Pages: "+str(nbPages)+" in total"
    text_data_f = "\n\n".join(texts)

    st.info(totalPages)
    st.download_button("Download txt file", text_data_f)

    st.markdown('''
        <style>
        .btn{
            display: inline-flex;
            -moz-box-align: center;
            align-items: center;
            -moz-box-pack: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.25rem;
            margin: 0px;
            line-height: 1.6;
            color: rgb(49, 51, 63);
            background-color: #fff;
            width: auto;
            user-select: none;
            border: 1px solid rgba(49, 51, 63, 0.2);
            }
        .btn:hover{
            color: #00acee;
            background-color: #fff;
            border: 1px solid #00acee;
        }
        </style>
    ''',
    unsafe_allow_html=True
    )
