def should_escalate(
        query,
        retrieved_docs):

    sensitive = [
        "refund",
        "billing",
        "legal",
        "account access",
        "duplicate charge"
    ]

    if len(retrieved_docs) == 0:
        return True

    if any(
            word in query.lower()
            for word in sensitive
    ):
        return True

    return False


def handoff_summary(
        persona,
        query,
        docs):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": docs,
        "attempted_steps": [
            "Persona Detection",
            "Knowledge Base Retrieval",
            "Adaptive Response Generation"
        ],
        "recommendation":
            "Human Support Review Required"
    }