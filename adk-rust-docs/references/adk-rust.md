# ADK-Rust Reference Index

Welcome to the ADK-Rust (Agent Development Kit for Rust) v0.4 documentation. This framework is designed for building modular, production-ready AI agents with native Rust performance.

## Documentation Modules

Explore specific areas of the framework:

### [1. Core & Runtime](core.md)
Foundational traits, typed identity (`AdkIdentity`), the `Runner` execution engine, session management, state scoping (`user:`, `app:`, `temp:`), event logging, and binary artifacts.

### [2. Agents & Orchestration](agents.md)
Configuring `LlmAgent`, deterministic `WorkflowAgents` (Sequential, Parallel, Loop), hierarchical `Multi-Agent` systems, and LangGraph-style `GraphAgents`.

### [3. Tools & Capabilities](tools.md)
Extending agents with `#[tool]` macro functions, `BrowserToolset` for web automation, `McpToolset` for universal connectivity, `RagTool` for knowledge retrieval, and `adk-ui` for dynamic components.

### [4. Model Providers](models.md)
Interchangeable providers for Gemini (default), OpenAI (GPT-5), Anthropic (Claude), DeepSeek, and Groq. Includes local inference via Ollama and native `mistral.rs`.

### [5. Deployment & Observability](deployment.md)
Running agents via the `Launcher`, exposing REST APIs, A2A (Agent-to-Agent) protocol support, and production telemetry with OpenTelemetry.

### [6. Visual Development](studio.md)
Using **ADK Studio** to design workflows visually with action nodes (HTTP, Database, Code) and triggers (Webhook, Schedule, Event).

### [7. Guides & Best Practices](guides.md)
Scaffolding new projects, development standards (Rust 2024 edition), and the `adk-eval` framework for agent testing.

---

## Core Mandates for Developers

1. **Safety**: Use `AdkIdentity` for all session operations to ensure multi-tenant isolation.
2. **Context**: Use `temp:` state for turn-level data to keep the persistent context clean.
3. **Multimodal**: Use `before_model` callbacks to inject non-text artifacts (images/PDFs) directly into model requests.
4. **Resilience**: Configure `retry_budget` and `circuit_breaker_threshold` for all production tools.
