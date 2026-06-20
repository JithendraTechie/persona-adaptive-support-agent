# Persona-Adaptive Customer Support Agent

## Project Overview

The Persona-Adaptive Customer Support Agent is an AI-powered support system that adapts its responses based on the user's persona. The system uses Retrieval-Augmented Generation (RAG) principles to retrieve relevant support documentation and provide personalized responses.

The application identifies different user personas, retrieves relevant knowledge base documents using semantic search, generates persona-specific responses, and escalates sensitive issues to human support when necessary.

---

## Features

### Persona Detection

The system automatically classifies users into one of the following personas:

* Technical Expert
* Frustrated User
* Business Executive

### Knowledge Base Retrieval (RAG)

* Uses ChromaDB as a vector database
* Uses Sentence Transformers for document embeddings
* Retrieves the most relevant support documents based on user queries

### Personalized Response Generation

Responses are adapted according to the detected persona:

* Technical Experts receive detailed troubleshooting information
* Frustrated Users receive empathetic and simplified guidance
* Business Executives receive concise business-focused summaries

### Human Escalation

The system automatically escalates sensitive requests such as:

* Refund requests
* Billing issues
* Duplicate charges
* Legal concerns
* Account access issues

---

## Project Architecture

```text
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
```

---

## Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Frontend         | Streamlit             |
| Language         | Python                |
| Vector Database  | ChromaDB              |
| Embeddings       | Sentence Transformers |
| Retrieval Method | RAG                   |
| Knowledge Base   | Local Text Documents  |

---

## Folder Structure

```text
persona-adaptive-support-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── account_lockout.txt
│   ├── api_authentication.txt
│   ├── billing_policy.txt
│   ├── cloud_uptime.txt
│   ├── integration_errors.txt
│   ├── password_reset.txt
│   ├── payment_failures.txt
│   ├── security_policy.txt
│   ├── subscription_faq.txt
│   └── user_management.txt
│
└── src/
    ├── __init__.py
    ├── classifier.py
    ├── rag.py
    ├── generator.py
    └── escalator.py
```

---

## Persona Detection Logic

### Technical Expert

Detected using keywords such as:

* API
* Authentication
* Logs
* Configuration
* Error
* Integration

### Frustrated User

Detected using keywords such as:

* Frustrated
* Angry
* Nothing works
* Urgent
* Tried everything

### Business Executive

Default persona when no specific technical or frustration indicators are detected.

---

## RAG Implementation

### Document Ingestion

The application loads support documents from the `data/` directory.

### Embedding Generation

Documents are converted into vector embeddings using:

```python
all-MiniLM-L6-v2
```

### Vector Storage

Embeddings are stored in ChromaDB for efficient semantic retrieval.

### Retrieval

For every user query:

1. Query embedding is generated.
2. Similarity search is performed.
3. Top relevant documents are retrieved.
4. Retrieved content is used for response generation.

---

## Escalation Strategy

The application automatically escalates issues involving:

* Refund requests
* Billing disputes
* Legal concerns
* Duplicate charges
* Account access problems

Example:

```text
I need a refund for a duplicate charge on my subscription.
```

Output:

```text
Escalated To Human Agent
```

---

## Example Scenarios

### Scenario 1 – Technical Expert

User Query:

```text
API authentication keeps failing with a 401 error.
```

Detected Persona:

```text
Technical Expert
```

Retrieved Sources:

```text
api_authentication.txt
integration_errors.txt
cloud_uptime.txt
```

---

### Scenario 2 – Frustrated User

User Query:

```text
I'm frustrated. Nothing works and I cannot reset my password.
```

Detected Persona:

```text
Frustrated User
```

Retrieved Sources:

```text
password_reset.txt
api_authentication.txt
integration_errors.txt
```

---

### Scenario 3 – Business Executive

User Query:

```text
What is the impact of the recent service disruption?
```

Detected Persona:

```text
Business Executive
```

Retrieved Sources:

```text
cloud_uptime.txt
billing_policy.txt
payment_failures.txt
```

---

## Screenshots

Add screenshots here before submission.

Example:

```md
![Home Page](screenshots/homepage.png)

![Technical Expert Response](screenshots/technical_response.png)

![Escalation Example](screenshots/escalation.png)
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/JithendraTechie/persona-adaptive-support-agent.git
```

### Navigate to Project

```bash
cd persona-adaptive-support-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Improvements

* Integrate a production-grade LLM
* Add conversation history support
* Improve persona detection using machine learning
* Add multi-language support
* Deploy using Streamlit Cloud or Render
* Add analytics dashboard for support monitoring

---

## Author

**Jithendra Vankayalapati**

B.Tech CSE (AI & ML)

Project developed as part of the Adsparx AI Engineering Screening Assignment.
