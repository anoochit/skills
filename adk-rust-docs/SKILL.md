# ADK-Rust Docs

## Overview

This skill provides comprehensive documentation and code patterns for **ADK-Rust** (Agent Development Kit for Rust) v0.4, a modular framework for building production-ready AI agents.

## Core Concepts

ADK-Rust is built on a layered architecture:
1. **Application**: CLI, REST API (Axum), or Realtime Voice.
2. **Runner**: The execution engine (`Launcher`) that manages flows, sessions, and tools.
3. **Agent**: Reasoning logic (`LlmAgent`, `GraphAgent`, `WorkflowAgent`).
4. **Service**: Models, Tools, RAG, and Memory backends.

## Usage

When working with ADK-Rust, reference these files for specific details:

- **[references/llms.txt](references/llms.txt)**: Ultra-compact architecture and v0.4 quickstart.
- **[references/adk-rust.md](references/adk-rust.md)**: Main reference index.
- **[references/core.md](references/core.md)**: Core primitives, Identity, Runner, and State Scoping.
- **[references/agents.md](references/agents.md)**: LlmAgent, Graph, Workflow, Multi-Agent, and Realtime.
- **[references/tools.md](references/tools.md)**: `#[tool]` macro, Browser, MCP, RAG, and UI Tools.
- **[references/models.md](references/models.md)**: Cloud Providers (Gemini, OpenAI, etc.) and Local Models.
- **[references/deployment.md](references/deployment.md)**: Launcher, Server API, A2A, and Telemetry.
- **[references/studio.md](references/studio.md)**: ADK Studio, Action Nodes, and Triggers.
- **[references/guides.md](references/guides.md)**: Project Standards and Agent Evaluation.

## Common Patterns

### Zero-Boilerplate Tool (v0.4)
```rust
#[tool]
/// Get the current weather for a city.
async fn get_weather(args: WeatherArgs) -> Result<Value, AdkError> {
    Ok(json!({ "temp": 72, "city": args.city }))
}
```

### Graph Agent Workflow
```rust
let agent = GraphAgent::builder("processor")
    .node(translator_node)
    .edge(START, "translator")
    .edge("translator", END)
    .build()?;
```

### Realtime Voice Agent
```rust
let agent = RealtimeAgent::builder("voice_bot")
    .model(openai_realtime_model)
    .voice("alloy")
    .server_vad()
    .build()?;
```

### Local Inference with mistral.rs (Native)
```rust
let config = MistralRsConfig::builder()
    .model_source(ModelSource::huggingface("microsoft/Phi-3.5-mini-instruct"))
    .isq(QuantizationLevel::Q4_0)
    .build();
let model = MistralRsModel::new(config).await?;
```
