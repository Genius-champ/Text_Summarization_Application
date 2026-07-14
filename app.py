"""
==========================================================
AI TEXT SUMMARIZATION SYSTEM
Author: Ikeoluwa Akanmu
Framework:
    - Streamlit
    - LangChain 1.x
    - OpenAI
==========================================================
"""

import time
import streamlit as st

from summarizer import summarize_text, summarize_pdf

from helpers import (
    calculate_statistics
)

from downloads import (
    download_txt,
    download_docx,
    download_pdf
)

###########################################################
# PAGE CONFIGURATION
###########################################################

st.set_page_config(
    page_title="AI Text Summarization",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

###########################################################
# CUSTOM CSS
###########################################################

st.markdown("""
<style>

.main{
    background-color:#F4F8FB;
}

h1{
    color:#002147;
}

h2,h3{
    color:#003366;
}

.stButton>button{
    background:#003366;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:17px;
    font-weight:bold;
}

.stDownloadButton>button{
    background:#C69214;
    color:white;
    border-radius:8px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0px 0px 8px rgba(0,0,0,0.10);
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

###########################################################
# SIDEBAR
###########################################################

with st.sidebar:

    st.image(
        "assets/Logo.png",
        width=180
    )

    st.title("AI Summarizer")

    st.markdown("## AI Text Summarizer")
        """
This application performs academic text summarization
using OpenAI Large Language Models.

Supported Inputs

• Plain Text

• PDF Documents

Map-Reduce summarization is used
to summarize large documents.
"""
    )

###########################################################
# MAIN HEADER
###########################################################

st.image(
    "assets/Banner.png",
    use_container_width=True
)

st.title(" AI Text Summarization")

st.write(
"""
Generate concise summaries of long academic
documents using OpenAI and LangChain.
"""
)

###########################################################
# INPUT TYPE
###########################################################

input_type = st.radio(

    "Choose Input Type",

    [

        "Paste Text",

        "Upload PDF"

    ],

    horizontal=True

)

###########################################################
# SUMMARY OPTIONS
###########################################################

summary_length = st.selectbox(

    "Summary Length",

    [

        "Short",

        "Medium",

        "Long"

    ]

)

###########################################################
# TEXT INPUT
###########################################################

text = ""

uploaded_pdf = None

if input_type == "Paste Text":

    text = st.text_area(

        "Enter text",

        height=300,

        placeholder="Paste your text here..."

    )

else:

    uploaded_pdf = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )

###########################################################
# SUMMARIZE BUTTON
###########################################################

if st.button("Generate Summary"):

    if input_type == "Paste Text":

        if text.strip() == "":

            st.warning("Please enter some text.")

            st.stop()

    else:

        if uploaded_pdf is None:

            st.warning("Please upload a PDF.")

            st.stop()

    start = time.time()

    progress = st.progress(0)

    with st.spinner("Summarizing document..."):

        progress.progress(20)

        if input_type == "Paste Text":

            summary = summarize_text(

                text=text,

                summary_length=summary_length

            )

            original_text = text

        else:

            summary, original_text = summarize_pdf(

                uploaded_pdf,

                summary_length

            )

        progress.progress(90)

    elapsed = time.time() - start

    progress.progress(100)

    ########################################################
    # STATISTICS
    ########################################################

    stats = calculate_statistics(

        original_text,

        summary,

        elapsed

    )

    st.success("Summary Generated Successfully")

    st.divider()

    st.subheader("Summary")

    st.write(summary)

    st.divider()

    ########################################################
    # METRICS
    ########################################################

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(

        "Original Words",

        stats["original_words"]

    )

    col2.metric(

        "Summary Words",

        stats["summary_words"]

    )

    col3.metric(

        "Compression",

        stats["compression_ratio"]

    )

    col4.metric(

        "Processing Time",

        stats["processing_time"]

    )

    st.divider()

    ########################################################
    # DOWNLOADS
    ########################################################

    st.subheader("Download Summary")

    d1, d2, d3 = st.columns(3)

    with d1:

        download_txt(summary)

    with d2:

        download_docx(summary)

    with d3:

        download_pdf(summary)

###########################################################
# FOOTER
###########################################################

st.markdown("---")

st.caption(
"""
Developed using

• Streamlit

• LangChain 1.x

• OpenAI GPT Models
"""
)
