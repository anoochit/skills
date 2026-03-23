# ADK-Rust Models

Reference for cloud and local LLM providers supported by `adk-model`.

## Cloud Providers

All providers implement the `Llm` trait and are interchangeable.

### Gemini (Google) ⭐ Default
- **Key Models**: `gemini-3-pro`, `gemini-3-flash`, `gemini-2.5-flash`.
- **Features**: 2M context, native multimodal (PDF/Audio/Video), thinking mode (level or budget based).

### OpenAI (GPT-5)
- **Key Models**: `gpt-5`, `gpt-5-mini`, `o3-mini`.
- **Features**: Industry standard, excellent tool calling, reasoning effort control for `o*` models.

### Anthropic (Claude)
- **Key Models**: `claude-sonnet-4-5-20250929`, `claude-opus-4-5-20251101`.
- **Features**: High reasoning quality, most safety-focused.

### DeepSeek
- **Key Models**: `deepseek-chat`, `deepseek-reasoner`.
- **Features**: Cost-effective, thinking mode (chain-of-thought) included in responses.

### Groq
- **Key Models**: `llama-4-scout`, `llama-3.1-70b-versatile`.
- **Features**: Ultra-fast inference using LPU technology.

---

## Local Models

### Ollama
Run models locally with privacy and zero cost.
```rust
let model = OllamaModel::new(OllamaConfig::new("llama3.2"))?;
```
- **Requirements**: `ollama serve` running locally.
- **Best Tool Calling**: `qwen2.5:7b` or `qwen3:14b`.

### mistral.rs (Native Inference)
High-performance local inference without external daemons.
```rust
let config = MistralRsConfig::builder()
    .model_source(ModelSource::huggingface("microsoft/Phi-3.5-mini-instruct"))
    .isq(QuantizationLevel::Q4_0) // Reduce memory
    .build();
let model = MistralRsModel::new(config).await?;
```
- **Acceleration**: Automatic Metal (macOS) or CUDA feature flag.
- **Features**: Vision models, LoRA adapter hot-swapping, multi-model serving.
