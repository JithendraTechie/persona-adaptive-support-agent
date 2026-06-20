def generate_response(persona, documents):

    context = "\n\n".join(documents)

    if persona == "Technical Expert":
        return f"""
Technical Analysis:

Based on the documentation:

{context}

Suggested troubleshooting:
1. Verify configuration.
2. Review logs.
3. Retry the operation.
"""

    elif persona == "Frustrated User":

        return """
I understand how frustrating this situation can be.

Please try these steps:

1. Reset your password using the Forgot Password option.

2. Check your email inbox and spam folder.

3. Wait a few minutes and try again.

4. If the issue continues, contact support for further assistance.

We are committed to helping you resolve this as quickly as possible.
"""
    else:
        return f"""
Business Summary:

{context}

Impact appears limited to the reported issue.
Further review can be performed if needed.
"""