# ADK-Rust Core

Reference for fundamental traits, the execution runtime, and state management.

## Core Types

### Content and Part
Every message is a `Content` object containing one or more `Part` items (Text, InlineData, FunctionCall, FunctionResponse).
- **Roles**: `user`, `model`, `tool`.
- **Multimodal**: `Part::InlineData` for bytes (images, audio, PDF) or `Part::FileData` for URIs.

### Identity Layers
ADK-Rust uses typed identifiers to prevent ID swapping:
1. **Auth Identity (`RequestContext`)**: Who is making the request?
2. **Session Identity (`AdkIdentity`)**: Stable address (AppName + UserId + SessionId).
3. **Execution Identity**: Runtime coordinates (Identity + InvocationId + AgentName).

---

## Runner (`adk-runner`)

The engine that orchestrates agent execution, session management, and tool calls.

### Configuration
```rust
let config = RunnerConfig {
    app_name: "my_app".to_string(),
    agent: root_agent,
    session_service: sessions,
    artifact_service: Some(artifacts),
    ..Default::default()
};
let runner = Runner::new(config)?;
```

### Context Compaction
Summarizes older events to keep the context window bounded.
- `compaction_interval`: Invocations between summaries.
- `overlap_size`: Events carried over for continuity.

---

## Sessions and State (`adk-session`)

### Scoped State Prefixes
- **`user:`**: Shared across all sessions for a user.
- **`app:`**: Shared across all users of an application.
- **`temp:`**: Cleared after each invocation (not persisted).
- **(none)**: Session-scoped (default).

### Typed Operations
```rust
session.state().set("user:theme".into(), json!("dark"));
let theme = session.state().get("user:theme");
```

---

## Events and Callbacks

### Event Structure
Immutable logs of interactions. Access content via `event.llm_response.content`.
- **`state_delta`**: State changes to apply.
- **`transfer_to_agent`**: Handoff signal.

### Callbacks
- **Agent**: `before_agent`, `after_agent`.
- **Model**: `before_model` (can modify request or skip/cache), `after_model`.
- **Tool**: `before_tool`, `after_tool` (rich V2 variant available).

---

## Artifacts (`adk-artifact`)

Storage for binary data with versioning and scoping.
- **Scoping**: Session-scoped by default; `user:` prefix for cross-session sharing.
- **Versioning**: Auto-incrementing version numbers per file.
- **Injection**: Use `before_model` callback to inject image/PDF artifacts into the LLM request.
