# Graph Report - Enterprise-IT-Support-Agentic-RAG-Copilot  (2026-10-15)

## Corpus Check
- Corpus is ~5,519 words - fits in a single context window. You may not need a graph.

## Summary
- 154 nodes · 284 edges · 26 communities (9 shown, 17 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Agentic RAG Workflow
- Free-Stack Docs & Deploy
- Key Rotation & Failover
- FAISS Vectorstore
- Frontend Chat UI
- FastAPI App Bootstrap
- App Config & Settings
- Ingest API & Lifespan
- Chat API Routes
- Audit Logging
- IT Handbook KB
- Runbook KB
- FDE Lifecycle
- NovaCore Reliability
- Demo Requirements
- RAG Problem Statement
- FDE Deck Document
- NovaCore Info Doc
- NovaCore Leave Policy

## God Nodes (most connected - your core abstractions)
1. `AgentState` - 19 edges
2. `build_graph()` - 15 edges
3. `add_trace()` - 12 edges
4. `get_settings()` - 11 edges
5. `llm()` - 11 edges
6. `add_documents()` - 9 edges
7. `ask()` - 8 edges
8. `load_file()` - 8 edges
9. `google_keys()` - 7 edges
10. `next_google_key()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Agent trace panel with final source` --conceptually_related_to--> `Agentic RAG control loop route retrieve grade rewrite`  [INFERRED]
  templates/index.html → README.md
- `Company document upload modal` --conceptually_related_to--> `FAISS local private knowledge base`  [INFERRED]
  templates/index.html → README.md
- `ask()` --uses--> `AgentState`  [INFERRED]
  app/rag/workflow.py → app/rag/state.py
- `Sixteen step build pipeline` --references--> `Employee chat UI with workflow sidebar`  [EXTRACTED]
  steps.md → templates/index.html
- `chat()` --calls--> `ask()`  [EXTRACTED]
  app/api/routes.py → app/rag/workflow.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **FDE delivery lifecycle** — docs_forward_deployed_engineer_explained_pptx_fde_role, docs_forward_deployed_engineer_explained_pptx_fde_lifecycle [INFERRED 0.75]
- **Agentic RAG route retrieve grade fallback rewrite generate loop** — readme_agentic_rag_control_loop, readme_faiss_private_kb, readme_duckduckgo_web_fallback, readme_gemini_llm_primary [EXTRACTED 0.75]
- **Chat UI plus trace panel plus upload modal flow** — templates_index_employee_chat_ui, templates_index_agent_trace_panel, templates_index_document_upload_modal [EXTRACTED 0.75]

## Communities (26 total, 17 thin omitted)

### Community 0 - "Agentic RAG Workflow"
Cohesion: 0.21
Nodes (21): AgentState, EvidenceGrade, RouteDecision, add_trace(), after_kb(), after_web(), build_graph(), direct_answer() (+13 more)

### Community 1 - "Free-Stack Docs & Deploy"
Cohesion: 0.16
Nodes (15): Agentic RAG control loop route retrieve grade rewrite, DuckDuckGo web search fallback, Enterprise IT Support Agentic RAG Copilot, FAISS local private knowledge base, FastAPI backend with chat ingest health APIs, Gemini Flash-Lite primary LLM and embeddings, Groq gpt-oss-20b automatic fallback, NovaRetail repetitive ticket problem (+7 more)

### Community 2 - "Key Rotation & Failover"
Cohesion: 0.19
Nodes (6): google_keys(), groq_key(), next_google_key(), ask(), groq_llm(), _is_quota_error()

### Community 3 - "FAISS Vectorstore"
Cohesion: 0.22
Nodes (5): add_documents(), get_embeddings(), get_retriever(), get_vectorstore(), _index_path()

### Community 4 - "Frontend Chat UI"
Cohesion: 0.24
Nodes (12): addMessage(), askAgent(), asText(), chat, escapeHtml(), form, formatText(), modal (+4 more)

### Community 8 - "Ingest API & Lifespan"
Cohesion: 0.32
Nodes (4): ingest(), lifespan(), chunk_documents(), load_file()

### Community 9 - "Chat API Routes"
Cohesion: 0.33
Nodes (3): chat(), ChatRequest, health()

### Community 11 - "IT Handbook KB"
Cohesion: 0.50
Nodes (4): Company IT Handbook document, MFA Policy, Password Reset Policy, VPN Access Policy

### Community 12 - "Runbook KB"
Cohesion: 0.67
Nodes (3): Service Desk Runbook document, Email Troubleshooting, Ticket Priority Levels

## Knowledge Gaps
- **17 isolated node(s):** `VPN Access Policy`, `Password Reset Policy`, `MFA Policy`, `Ticket Priority Levels`, `Email Troubleshooting` (+12 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 66 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_settings()` connect `App Config & Settings` to `Agentic RAG Workflow`, `Key Rotation & Failover`, `FAISS Vectorstore`, `FastAPI App Bootstrap`, `Chat API Routes`, `Audit Logging`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `AgentState` (e.g. with `add_trace()` and `after_kb()`) actually correct?**
  _`AgentState` has 16 INFERRED edges - model-reasoned connections that need verification._
- **What connects `VPN Access Policy`, `Password Reset Policy`, `MFA Policy` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `add_documents()` connect `FAISS Vectorstore` to `Ingest API & Lifespan`, `Chat API Routes`, `FastAPI App Bootstrap`, `App Config & Settings`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Are the 14 inferred relationships involving `build_graph()` (e.g. with `AgentState` and `after_kb()`) actually correct?**
  _`build_graph()` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Why does `next_google_key()` connect `Key Rotation & Failover` to `Agentic RAG Workflow`, `FAISS Vectorstore`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._