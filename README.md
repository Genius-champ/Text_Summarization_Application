# Text_Summarization_Application

## Overview

The **AI Text_Summarization_Application** is a web-based application that automatically generates concise summaries from long documents using Large Language Models (LLMs).

The application uses:

- Streamlit for the user interface
- LangChain 1.x for LLM orchestration
- OpenAI GPT models for summarization
- Map-Reduce summarization methodology for processing long documents

The system supports both:

- Direct text input
- PDF document upload

Users can generate summaries and download them in multiple formats.

---

#  Features

## Input Options

 Paste text directly into the application

 Upload PDF documents


## Summarization

 Map-Reduce summarization workflow

 LangChain 1.x compatible implementation

 OpenAI GPT-powered summaries

 Adjustable summary length:

- Short
- Medium
- Long


## Summary Statistics

The application provides:

- Original document word count
- Generated summary word count
- Compression ratio
- Processing time


## Export Options

Generated summaries can be downloaded as:

- TXT
- DOCX
- PDF


## User Interface

The application includes:

- Academic-style interface
- University-inspired color theme
- Sidebar navigation
- Progress indicators
- Responsive layout

---

#  Project Structure


TextSummarizationApp/

│
├── app.py
│ Main Streamlit application
│
├── summarizer.py
│ LangChain Map-Reduce summarization logic
│
├── helpers.py
│ Statistics and utility functions
│
├── downloads.py
│ TXT, DOCX, and PDF export functions
│
├── requirements.txt
│ Required Python packages
│
├── assets/
│ Images and UI resources
│
└── .streamlit/
Streamlit configuration files


---

#  Technology Stack

## Frontend

- Streamlit


## Artificial Intelligence

- OpenAI GPT Models
- LangChain 1.x


## Document Processing

- PyPDF


## File Generation

- python-docx
- ReportLab


## Programming Language

- Python 3.11+

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TextSummarizationApp.git

Move into the project directory:

cd TextSummarizationApp
2. Create a Virtual Environment
python -m venv venv

Activate it:

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
 OpenAI API Configuration

The application uses Streamlit Secrets to protect the OpenAI API key.

Local Development

Create:

.streamlit/secrets.toml

Add:

OPENAI_API_KEY="your-openai-api-key"

Do not upload this file to GitHub.

 Running the Application Locally

Run:

streamlit run app.py

The application will open in your browser:

http://localhost:8501
 Deploying on Streamlit Community Cloud
Step 1: Push Project to GitHub

Your repository should contain:

app.py
summarizer.py
helpers.py
downloads.py
requirements.txt
README.md
assets/
.streamlit/config.toml

Do not upload:

.streamlit/secrets.toml
Step 2: Create Streamlit Application
Go to Streamlit Community Cloud
Select:
New app
Choose:
Repository:
YOUR_USERNAME/TextSummarizationApp

Branch:
main

Main file:
app.py
Click:
Deploy
Step 3: Add API Key

After deployment:

Open:

App Settings
        |
        └── Secrets

Add:

OPENAI_API_KEY="your-openai-api-key"

Save and restart the application.

 Security Notes

Never store API keys:

Inside Python files
Inside GitHub repositories
Inside requirements.txt

Use:

st.secrets["OPENAI_API_KEY"]

for secure access.

 Application Workflow
User Input
    |
    |
Text / PDF Upload
    |
    |
Document Splitting
    |
    |
MAP Phase
(each section summarized)
    |
    |
REDUCE Phase
(combine summaries)
    |
    |
Final Summary
    |
    |
Download Output
 Future Improvements

Possible future enhancements:

Additional language support
Multiple document uploads
Improved document formatting
Additional AI model options
Author

Developed using:

Streamlit
LangChain
OpenAI GPT

---

# Current Project Status

Your project now contains:

```text
TextSummarizationApp/

│
├── app.py                 
├── summarizer.py          
├── helpers.py             
├── downloads.py           
├── requirements.txt       
├── README.md              
│
├── assets/
│   ├── logo.png           
│   └── banner.png         
│
└── .streamlit/
    └── config.toml        
