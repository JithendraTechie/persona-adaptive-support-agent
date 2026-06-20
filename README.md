# Persona-Adaptive Customer Support Agent

## Project Overview

This project is an AI-powered customer support agent that detects customer personas, retrieves relevant information from a support knowledge base, generates persona-aware responses, and escalates unresolved issues to human support representatives.

Supported Personas:

* Technical Expert
* Frustrated User
* Business Executive

The system uses Retrieval-Augmented Generation (RAG), persona detection, adaptive response generation, and human escalation workflows.

---

## Tech Stack

* Python 3.10+
* Streamlit
* ChromaDB
* Sentence Transformers
* LangChain
* PyPDF
* Python Dotenv

---

## Architecture

User Query
↓
Persona Detection
↓
Knowledge Base Retrieval
↓
Adaptive Response Generation
↓
Escalation Check
↓
Human Handoff Summary

---

## Persona Detection Strategy

Rule-based classification using keywords.

Technical Expert:

* API
* Logs
* Authentication
* Configuration

Frustrated User:

* Frustrated
* Angry
* Urgent
* Tried Everything

Business Executive:

* Default classification
* Outcome-oriented queries

---

## RAG Pipeline

1. Load support documents
2. Generate document embeddings
3. Store vectors in ChromaDB
4. Retrieve top matching documents
5. Generate grounded responses

---

## Escalation Logic

Escalation occurs when:

* Refund requests are detected
* Billing issues are reported
* Legal issues are reported
* Account-sensitive requests occur
* No relevant information is available

---

## Setup

pip install -r requirements.txt

streamlit run app.py

---

## Example Queries

1. Explain API authentication error and logs.
2. I am frustrated and nothing works.
3. How does this issue impact operations?
4. I need a refund for a duplicate charge.
5. Why is my account locked?

---

## Knowledge Base

The project includes:

* Password Reset Guide
* API Authentication Guide
* Billing Policy
* Subscription FAQ
* Cloud Uptime Guide
* Integration Errors Guide
* Payment Failures Guide
* Security Policy
* User Management Guide
* Account Lockout Guide

---

## Future Improvements

* LLM-powered persona classification
* Multi-turn conversation memory
* Confidence scoring
* LangGraph workflow orchestration
* Human approval workflows
* Analytics dashboard
