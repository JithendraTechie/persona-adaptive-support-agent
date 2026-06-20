Persona-Adaptive Customer Support Agent
Project Overview

This project is a Persona-Adaptive Customer Support Agent that automatically identifies the user's persona, retrieves relevant support documentation using Retrieval-Augmented Generation (RAG), generates persona-specific responses, and escalates sensitive issues to human support agents.

The solution is designed to improve customer support experiences by adapting communication styles to different user types.

Problem Statement

Traditional customer support systems provide the same response style to every user.

This project solves that problem by:

Detecting user persona
Retrieving relevant support knowledge
Generating personalized responses
Escalating sensitive issues
Features
Persona Detection

The system classifies users into:

Technical Expert
Frustrated User
Business Executive
Knowledge Retrieval

Uses:

Sentence Transformers
ChromaDB Vector Database

to retrieve the most relevant support documents.

Response Generation

Responses are customized according to the detected persona.

Escalation Logic

Automatically escalates:

Refund requests
Billing issues
Legal concerns
Duplicate charges
Account access issues
Project Architecture

User Query
↓
Persona Detection
↓
Document Retrieval (RAG)
↓
Response Generation
↓
Escalation Check
↓
Final Response / Human Handoff

Tech Stack
Component	Technology
Frontend	Streamlit
Vector Database	ChromaDB
Embeddings	Sentence Transformers
Language	Python
Retrieval	RAG
Storage	Local Knowledge Base
Folder Structure
persona-adaptive-support-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│ ├── password_reset.txt
│ ├── billing_policy.txt
│ ├── payment_failures.txt
│ ├── api_authentication.txt
│ ├── cloud_uptime.txt
│ └── ...
│
├── src/
│ ├── classifier.py
│ ├── rag.py
│ ├── generator.py
│ ├── escalator.py
│ └── init.py
│
└── chroma_db/
Persona Detection Logic

Technical Expert

Detected using keywords:

API
Authentication
Configuration
Logs
Integration

Frustrated User

Detected using keywords:

Frustrated
Angry
Nothing works
Urgent
Tried everything

Business Executive

Default classification when no other persona is detected.

RAG Implementation

Documents are stored in the data folder.

Workflow:

Load support documents
Generate embeddings
Store embeddings in ChromaDB
Retrieve top matching documents
Generate persona-specific responses
Escalation Strategy

The system escalates requests when:

No relevant documents are found
Query contains refund requests
Billing disputes exist
Legal concerns are mentioned
Duplicate charges are reported

A handoff summary is generated for human support agents.

Example Scenarios
Technical Expert

Query:

Explain API authentication failure and provide error details.

Output:

Technical analysis
Configuration guidance
Log review suggestions
Frustrated User

Query:

I am frustrated and nothing works.

Output:

Empathetic response
Clear troubleshooting steps
Business Executive

Query:

How does this issue impact operations?

Output:

Business-focused summary
Operational impact analysis
Escalation Example

Query:

I need a refund for a duplicate charge.

Output:

Escalated to human support
Handoff summary generated
Results

Successfully implemented:

✅ Persona Detection

✅ Retrieval-Augmented Generation (RAG)

✅ Knowledge Base Search

✅ Personalized Responses

✅ Human Escalation Workflow

✅ Streamlit User Interface

Future Improvements
LLM-powered response generation using Gemini
Advanced sentiment analysis
Multi-language support
Conversation memory
Analytics dashboard
How To Run
pip install -r requirements.txt
streamlit run app.py

Application will be available at:

http://localhost:8501
Author

Jithendra Vankayalapati

B.Tech CSE (AI & ML)
