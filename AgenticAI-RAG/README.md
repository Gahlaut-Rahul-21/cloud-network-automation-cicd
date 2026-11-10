# Agentic AI and RAG

> Status: placeholder. Demo project to be added.

Demos of Retrieval-Augmented Generation (RAG) and tool-using AI agents, built entirely on open-source models and libraries that run locally.

## Scope

- **RAG:** document loading, chunking, embeddings, vector search, grounded answers with citations
- **Agents:** tool calling, planning loops, memory, guardrails
- **Evaluation:** retrieval quality and answer faithfulness

## Planned demo

A network-operations assistant that answers questions over runbooks and device docs, and can call tools.

1. Ingest markdown and PDF runbooks into a vector store
2. Answer questions with retrieved context and source references
3. Agent tools: subnet calculator, config-diff viewer, read-only device status lookup
4. Basic evaluation set to measure retrieval hit rate

## Open-source stack

| Purpose | Tool |
|---|---|
| Local LLM runtime | [Ollama](https://ollama.com) or llama.cpp |
| Orchestration | LangChain or LlamaIndex |
| Embeddings | sentence-transformers |
| Vector store | ChromaDB or FAISS |
| Agent framework | LangGraph |
| API / UI | FastAPI, Streamlit |
| Evaluation | RAGAS, pytest |

## Proposed layout

```
AgenticAI-RAG/
├── data/          # sample documents
├── ingest/        # loaders, chunking, indexing
├── rag/           # retriever and answer chain
├── agent/         # tools and agent graph
├── eval/          # test questions and metrics
├── tests/
└── README.md
```

## Learning outcomes

- Understand why RAG reduces hallucination and where it still fails
- Design safe agent tools with clear inputs, outputs and limits
- Measure quality instead of judging by feel
