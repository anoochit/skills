# ADK-Rust Guides

Reference for getting started, development best practices, and evaluation.

## Quickstart

Scaffold a new project in seconds:
```bash
cargo install cargo-adk
cargo adk new my_agent --template tools
```

### Core Flow
1. **Initialize Model**: `GeminiModel::new(&key, "gemini-2.5-flash")`.
2. **Build Agent**: `LlmAgentBuilder::new("bot").model(model).build()`.
3. **Run Launcher**: `Launcher::new(agent).run().await`.

---

## Development Guidelines

### Project Standards
- **Rust Edition**: 2024 (Rust 1.85.0+).
- **Error Handling**: Use `adk_core::AdkError`.
- **Async**: Use `tokio` (minimal features in libraries).
- **Testing**: Use `cargo-nextest` for parallel execution.

### Contribution Process
1. **Format**: `cargo fmt --all`.
2. **Lint**: `cargo clippy --all-targets`.
3. **Test**: `cargo nextest run --workspace`.

---

## Agent Evaluation (`adk-eval`)

Testing probabilistic LLM behavior with structured metrics.

### Evaluation Strategies
- **Trajectory**: Validate tool call sequences.
- **Similarity**: Compare responses (Jaccard, Levenshtein, ROUGE).
- **LLM Judge**: Use a second LLM to assess quality/factual accuracy.
- **Rubrics**: Weighted scoring against custom criteria.

### Integration
Evaluations use `.test.json` files and can be integrated into standard `cargo test` suites for CI/CD validation.
