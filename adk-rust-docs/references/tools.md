# ADK-Rust Tools

Reference for extending agent capabilities with tools and toolsets.

## Function Tools

Custom Rust functions that the LLM can call.

### `#[tool]` Macro (Recommended)
Zero-boilerplate tool registration. Doc comments become descriptions; args structs become JSON schemas.
```rust
#[derive(Deserialize, JsonSchema)]
struct WeatherArgs { city: String }

/// Get the current weather for a city.
#[tool]
async fn get_weather(args: WeatherArgs) -> Result<Value, AdkError> {
    Ok(json!({ "temp": 72 }))
}
```

### Manual `FunctionTool`
```rust
let tool = FunctionTool::new("name", "desc", |ctx, args| async move { ... })
    .with_parameters_schema::<MyParams>();
```

---

## Browser Tools (`adk-browser`)

46 WebDriver-based tools for web automation.

### Features
- **Navigation**: `navigate`, `back`, `forward`, `refresh`.
- **Extraction**: `extract_text`, `extract_links`, `page_info`.
- **Interaction**: `click`, `type`, `select`, `drag_and_drop`.
- **Output**: `screenshot`, `print_to_pdf`.

### Pool-Backed Usage (Multi-Tenant)
```rust
let pool = Arc::new(BrowserSessionPool::new(config, 10));
let toolset = Arc::new(BrowserToolset::with_pool(pool));
agent_builder.toolset(toolset);
```

---

## MCP Tools (`adk-tool`)

Universal connectivity via Model Context Protocol.

### Usage
```rust
let client = ().serve(TokioChildProcess::new(cmd)?).await?;
let toolset = McpToolset::new(client).with_tools(&["read_file", "search"]);
agent_builder.toolset(Arc::new(toolset));
```

---

## RAG Tools (`adk-rag`)

Retrieval-Augmented Generation for searching knowledge bases.

### Pipeline Components
- **Chunkers**: `RecursiveChunker` (default), `MarkdownChunker`, `FixedSizeChunker`.
- **Embedders**: `GeminiEmbeddingProvider`, `OpenAIEmbeddingProvider`.
- **Vector Stores**: `InMemoryVectorStore`, `QdrantVectorStore`, `PgVectorStore`.

### Usage
```rust
let tool = RagTool::new(pipeline, "collection_name");
agent_builder.tool(Arc::new(tool));
```

---

## UI Tools (`adk-ui`)

Dynamic UI generation via A2UI JSONL.

### Available Tools
- `render_form`: Collect user input.
- `render_chart`: Bar, Line, Area, Pie charts.
- `render_table`: Present structured data.
- `render_screen`: Full A2UI surface.

### React Integration
Consumes JSONL messages to update a local `A2uiStore`.

---

## Code Execution (`adk-code`)

Isolated Rust execution with structured diagnostics.

### Components
- **`CodeTool`**: Compilation pipeline (check → build → execute).
- **`adk-sandbox`**: Isolation via `ProcessBackend` or `WasmBackend`.

### Usage
```rust
let executor = RustExecutor::new(backend, config);
let tool = CodeTool::new(executor);
agent_builder.tool(Arc::new(tool));
```
