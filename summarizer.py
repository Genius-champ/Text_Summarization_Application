"""
==========================================================
SUMMARIZER MODULE
Compatible with:
    - LangChain 1.x
    - OpenAI SDK 1.x
==========================================================
"""

import tempfile

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

###########################################################
# OPENAI MODEL
###########################################################

def get_llm():
    """
    Returns the OpenAI chat model.
    API key is read securely from Streamlit Secrets.
    """

    return ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=st.secrets["OPENAI_API_KEY"],
        temperature=0
    )


###########################################################
# PROMPTS
###########################################################

def get_map_prompt(summary_length):
    """
    Prompt used during the MAP phase.
    """

    lengths = {
        "Short": "Write a concise summary in approximately 100 words.",
        "Medium": "Write a detailed summary in approximately 250 words.",
        "Long": "Write a comprehensive summary in approximately 500 words."
    }

    return ChatPromptTemplate.from_template(
        f"""
You are an expert academic summarizer.

Summarize the following section.

Requirements:

{lengths[summary_length]}

Preserve:

- main ideas
- important findings
- important concepts

TEXT:

{{text}}
"""
    )


def get_reduce_prompt(summary_length):
    """
    Prompt used during the REDUCE phase.
    """

    lengths = {
        "Short": "Produce a concise final summary.",
        "Medium": "Produce a detailed final summary.",
        "Long": "Produce a comprehensive final summary."
    }

    return ChatPromptTemplate.from_template(
        f"""
You are an expert academic summarizer.

Below are summaries generated from different
parts of the same document.

Combine them into ONE coherent summary.

Requirements:

{lengths[summary_length]}

SUMMARIES:

{{summaries}}
"""
    )


###########################################################
# TEXT SPLITTER
###########################################################

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2500,
    chunk_overlap=250
)


###########################################################
# MAP-REDUCE SUMMARIZATION
###########################################################

def map_reduce(text, summary_length):
    """
    Performs Map-Reduce summarization.
    """

    llm = get_llm()

    chunks = splitter.split_text(text)

    map_prompt = get_map_prompt(summary_length)

    partial_summaries = []

    #######################################################
    # MAP STEP
    #######################################################

    for chunk in chunks:

        prompt = map_prompt.invoke(
            {
                "text": chunk
            }
        )

        response = llm.invoke(prompt)

        partial_summaries.append(
            response.content
        )

    #######################################################
    # REDUCE STEP
    #######################################################

    reduce_prompt = get_reduce_prompt(summary_length)

    final_prompt = reduce_prompt.invoke(
        {
            "summaries": "\n\n".join(partial_summaries)
        }
    )

    final_summary = llm.invoke(final_prompt)

    return final_summary.content


###########################################################
# TEXT SUMMARIZATION
###########################################################

def summarize_text(text, summary_length):
    """
    Summarizes plain text.
    """

    return map_reduce(
        text,
        summary_length
    )


###########################################################
# PDF SUMMARIZATION
###########################################################

def summarize_pdf(uploaded_pdf, summary_length):
    """
    Reads a PDF and summarizes it.
    """

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_pdf.read()
        )

        pdf_path = temp_file.name

    loader = PyPDFLoader(pdf_path)

    pages = loader.load()

    original_text = "\n".join(
        page.page_content
        for page in pages
    )

    summary = map_reduce(
        original_text,
        summary_length
    )

    return summary, original_text
