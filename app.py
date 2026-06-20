import streamlit as st

from src.classifier import detect_persona
from src.rag import (
    ingest_documents,
    retrieve
)

from src.generator import (
    generate_response
)

from src.escalator import (
    should_escalate,
    handoff_summary
)

ingest_documents()

st.set_page_config(
    page_title="Persona Adaptive Support Agent"
)

st.title(
    "Persona Adaptive Customer Support Agent"
)

query = st.chat_input(
    "Ask a support question"
)

if query:

    persona = detect_persona(
        query
    )

    results = retrieve(
        query
    )

    documents = (
        results["documents"][0]
        if results["documents"]
        else []
    )

    sources = []

    if results["metadatas"]:

        for meta in results["metadatas"][0]:

            sources.append(
                meta["source"]
            )

    st.subheader(
        "Detected Persona"
    )

    st.write(persona)

    st.subheader(
        "Retrieved Sources"
    )

    st.write(sources)

    escalation = should_escalate(
        query,
        documents
    )

    if escalation:

        st.error(
            "Escalated To Human Agent"
        )

        summary = handoff_summary(
            persona,
            query,
            sources
        )

        st.json(summary)

    else:

        response = generate_response(
            persona,
            documents
        )

        st.subheader(
            "Generated Response"
        )

        st.write(response)