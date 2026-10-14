from dataclasses import dataclass
from typing import Any, Dict, Optional

import chromadb

from src.services.embedding.service import EmbeddingService


@dataclass
class VectorDatabaseService:
    """Service for storing and retrieving text embeddings in ChromaDB."""

    embedding_service: Optional[EmbeddingService] = None
    vector_db_client: Optional[chromadb.PersistentClient] = None
    vector_db_collection: Optional[chromadb.Collection] = None
    collection_name: str = "bai_probie_vector_database"
    persist_directory: str = "vector_db_instance"

    def __post_init__(self):
        if self.vector_db_client is None:
            self.vector_db_client = chromadb.PersistentClient(
                path=self.persist_directory
            )

        if self.vector_db_collection is None:
            self.vector_db_collection = self.vector_db_client.get_or_create_collection(
                name=self.collection_name
            )
        if self.embedding_service is None:
            self.embedding_service = EmbeddingService()

    async def add_fact(self, text: str) -> str:
        """
        TODO: Add a fact to the vector database.

        Requirements:
        - Generate an id (use uuid.uuid4()) for the document
        - Call self.embedding_service.generate_embedding(text)
        - Add to `self.vector_db_collection` with ids, documents, embeddings
        - Return the generated id as a string
        """
        raise NotImplementedError("TODO: implement VectorDatabaseService.add_fact()")

    async def query(self, query_text: str, n_results: int = 10) -> Dict[str, Any]:
        """
        TODO: Query the vector database for similar documents.

        Requirements:
        - Generate an embedding for `query_text`
        - Call `self.vector_db_collection.query(...)` with:
          - query_embeddings=[the embedding]
          - n_results=n_results
          - include=["documents", "distances"]
        - Return the result dict
        """
        raise NotImplementedError("TODO: implement VectorDatabaseService.query()")

    async def format_query_results(self, query_result: chromadb.QueryResult) -> str:
        """
        TODO: Format query results into a string the LLM can consume.

        Requirements:
        - If there are no documents, return "No relevant documents found."
        - Otherwise, produce:
          "Relevant documents from the knowledge base:\n\n"
          followed by one block per document:
          <fact_1>\n{doc}\n</fact_1>\n\n
        - Return the final string (strip trailing whitespace)
        """
        raise NotImplementedError(
            "TODO: implement VectorDatabaseService.format_query_results()"
        )

    def clear(self) -> None:
        """Delete all facts from the vector database."""
        self.vector_db_client.delete_collection(name=self.collection_name)
        self.vector_db_collection = self.vector_db_client.create_collection(
            name=self.collection_name
        )
