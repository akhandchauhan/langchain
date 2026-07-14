# LangChain Models

Personal practice repo working through LangChain's core abstractions across multiple LLM providers — plain LLM completion, chat models, and embeddings/semantic similarity.

## What's in here

| Folder | Demonstrates |
|---|---|
| `1.LLMs/` | Base `LLM` interface (OpenAI `gpt-3.5-turbo-instruct` completion) |
| `2.ChatModels/` | `ChatModel` interface across providers: OpenAI (`gpt-4`), Anthropic (Claude), Google (`gemini-2.5-flash-lite`), and a Hugging Face inference endpoint (TinyLlama) |
| `3.EmbeddedModels/` | OpenAI embeddings — single query, batch documents, and a cosine-similarity search example (`4_document_similarity.py`) that ranks documents against a query |

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # or `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
```

Create a `.env` file in the project root with the API keys for whichever providers you want to run:

```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
HUGGINGFACEHUB_API_TOKEN=...
```

Then run any script directly, e.g.:

```bash
python "2.ChatModels/3_chatmodel_google.py"
```

## Why this exists

Each script isolates one concept (a single model call, a single embedding operation) so the LangChain abstraction being demonstrated is unambiguous — this is a learning/reference repo, not a packaged application.
