# ADK Studio

Reference for the visual development environment and deterministic workflow nodes.

## Overview

ADK Studio is a low-code interface for designing, testing, and deploying multi-agent workflows. It compiles visual designs directly to production Rust code.

### Installation
```bash
cargo install adk-studio
adk-studio --port 3000
```

---

## Action Nodes

14 non-LLM programmatic nodes for deterministic operations.

| Node | Icon | Description |
|------|------|-------------|
| **HTTP** | 🌐 | REST API calls with auth/headers/body. |
| **Database** | 🗄️ | SQL (Postgres/MySQL/SQLite) or NoSQL (Mongo/Redis). |
| **Code** | 💻 | Sandboxed JavaScript execution. |
| **Switch** | 🔀 | Conditional branching based on state. |
| **Loop** | 🔄 | Iterate over arrays or repeat tasks. |
| **Transform**| ⚙️ | JSONPath/Template data manipulation. |

### Variable Interpolation
All string fields support `{{variable}}` syntax, resolved from the workflow state at runtime.

---

## Triggers

Entry points that start a workflow.

- **Manual**: User-initiated via chat input.
- **Webhook**: HTTP endpoint (supports async or sync execution).
- **Schedule**: Cron-based timing (e.g., `0 9 * * *` for daily at 9 AM).
- **Event**: Response to external system events with JSONPath filtering.

---

## Code Generation

Studio generates standard `adk-rust` code:
- **Agents**: Mapped to `LlmAgentBuilder`.
- **Action Nodes**: Mapped to `adk-graph` `FunctionNode` closures.
- **Dependencies**: Automatically added to the generated `Cargo.toml`.
