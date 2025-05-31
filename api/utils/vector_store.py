from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os
load_dotenv()


def getVS():
    # initialize Qdrant's client
    client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY")
    )

    try:
        yield client
    finally:
        print("Vector Store initialized Successfully")