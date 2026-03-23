# ADK-Rust Agents

Comprehensive reference for building and orchestrating agents in ADK-Rust.

## LlmAgent

The `LlmAgent` is the core agent type that uses a Large Language Model for reasoning and decision-making.

### Basic Configuration
```rust
let agent = LlmAgentBuilder::new("my_agent")
    .instruction("You are a helpful assistant.")
    .model(Arc::new(model))
    .build()?;
```

### Instruction Templating
Supports `{var}`, `{prefix:var}`, `{var?}`, and `{artifact.file}`. Variables are resolved from session state at runtime.

### Tool Registration
```rust
.tool(Arc::new(weather_tool))
.toolset(Arc::new(browser_toolset)) // Resolved per invocation
```

### Builder Reference
- `max_iterations(n)`: Limit LLM round-trips (default: 100).
- `output_schema(json)`: Enforce structured output.
- `output_key(key)`: Save response to session state.
- `default_retry_budget(RetryBudget)`: Configure tool retries.
- `circuit_breaker_threshold(n)`: Disable tool after N consecutive failures.

---

## Workflow Agents

Deterministic agents that follow predefined execution paths.

### SequentialAgent
Runs sub-agents one after another. Each sees the accumulated history.
```rust
let pipeline = SequentialAgent::new(
    "pipeline",
    vec![Arc::new(researcher), Arc::new(writer)],
);
```

### ParallelAgent
Runs all sub-agents concurrently. Results stream as they complete.
```rust
let multi_analyst = ParallelAgent::new(
    "analyst",
    vec![Arc::new(tech), Arc::new(biz)],
);
```

### LoopAgent
Iterates until an exit condition is met or max iterations reached. Use `ExitLoopTool` to stop early.
```rust
let loop_agent = LoopAgent::new("refiner", vec![Arc::new(critic_refine)])
    .with_max_iterations(5);
```

---

## Multi-Agent Systems

Build hierarchies by delegating tasks to specialist agents.

### Sub-Agent Transfer
When sub-agents are added, the parent gains a `transfer_to_agent` tool.
```rust
let coordinator = LlmAgentBuilder::new("coordinator")
    .instruction("Route billing questions to billing_agent.")
    .sub_agent(Arc::new(billing_agent))
    .build()?;
```

### Hierarchical Flow
1. User sends message to Coordinator.
2. Coordinator calls `transfer_to_agent(agent_name="specialist")`.
3. Runner detects transfer and invokes the target agent immediately.

---

## Graph Agents

LangGraph-style orchestration for complex, stateful workflows with cycles and parallel execution.

### Core Components
- **Nodes**: `AgentNode` (wraps LLM agents) or `FunctionNode` (custom Rust code).
- **Edges**: `START`, `END`, static edges, or conditional routing via `Router`.
- **State**: Typed state with reducers (Overwrite, Append, Sum, Custom).
- **Checkpointing**: Persistence via `SqliteCheckpointer` or `MemoryCheckpointer`.

### Example
```rust
let agent = GraphAgent::builder("processor")
    .channels(&["input", "output"])
    .node(translator_node)
    .edge(START, "translator")
    .edge("translator", END)
    .build()?;
```

### Human-in-the-Loop
Pause execution for approval using `NodeOutput::interrupt_with_data` or `with_interrupt_before/after`.

---

## Realtime Voice Agents

Bidirectional audio streaming with OpenAI Realtime and Gemini Live.

### Supported Providers
- **OpenAI**: `gpt-4o-realtime-preview`, `gpt-realtime`. Transports: WebSocket, WebRTC.
- **Google**: `gemini-live-2.5-flash-native-audio`, Vertex AI Live.

### Configuration
```rust
let agent = RealtimeAgent::builder("assistant")
    .model(model)
    .voice("alloy")
    .server_vad() // Voice Activity Detection
    .tool(Arc::new(weather_tool))
    .on_audio(|chunk| { /* play audio */ })
    .build()?;
```

### Key Server Events
- `AudioDelta`: Audio chunk (base64 PCM).
- `TranscriptDelta`: Input audio transcript.
- `FunctionCallDone`: Tool call request.
