import os
import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    "support_docs"
)


def ingest_documents():

    existing = collection.count()

    if existing > 0:
        return

    for file in os.listdir("data"):

        if file.endswith(".txt"):

            path = os.path.join(
                "data",
                file
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            embedding = model.encode(
                text
            ).tolist()

            collection.add(
                ids=[file],
                documents=[text],
                embeddings=[embedding],
                metadatas=[
                    {
                        "source": file
                    }
                ]
            )


def retrieve(query):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results