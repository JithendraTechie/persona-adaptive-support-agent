def detect_persona(message):

    msg = message.lower()

    technical_words = [
        "api",
        "authentication",
        "logs",
        "configuration",
        "error",
        "integration"
    ]

    frustrated_words = [
        "frustrated",
        "angry",
        "nothing works",
        "urgent",
        "tried everything"
    ]

    if any(word in msg for word in technical_words):
        return "Technical Expert"

    elif any(word in msg for word in frustrated_words):
        return "Frustrated User"

    return "Business Executive"