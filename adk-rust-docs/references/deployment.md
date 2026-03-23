# ADK-Rust Deployment

Reference for deploying agents as servers and observing them in production.

## Launcher (`adk-cli`)

A one-line utility to run agents in interactive or server mode.

### Usage
```rust
Launcher::new(Arc::new(agent)).run().await?;
```

### CLI Modes
- **Console (default)**: `cargo run -- chat`.
- **Server**: `cargo run -- serve --port 8080`.

---

## Server API (`adk-server`)

REST API built on Axum for agent execution and session management.

### Key Endpoints
- `POST /api/run_sse`: Execute agent with Server-Sent Events streaming.
- `GET /api/sessions`: List sessions.
- `GET /ui/`: Built-in web interface for chat and session management.

---

## A2A Protocol

Agent-to-Agent communication across network boundaries.

### Agent Card
Automatically generated at `/.well-known/agent.json`. Describes capabilities and skills.

### Consuming Remote Agents
```rust
let remote = RemoteA2aAgent::builder("prime_checker")
    .agent_url("http://localhost:8001")
    .build()?;
agent_builder.sub_agent(Arc::new(remote));
```

---

## Telemetry (`adk-telemetry`)

Production observability via `tracing` and OpenTelemetry.

### Initialization
```rust
init_telemetry("my-service")?; // Console logging
init_with_otlp("my-service", "http://localhost:4317")?; // OTLP export
```

### Log Levels
Controlled via `RUST_LOG` env var (error, warn, info, debug, trace).

### Pre-configured Spans
Use `agent_run_span`, `model_call_span`, and `tool_execute_span` for standard ADK operations.
