---
name: uikits
description: Generate Flutter UI components from a curated list of templates. Use when the user wants to quickly scaffold common screens like Login, Signup, Profile, Feed, etc., in a Flutter application.
---

# uikits

This skill allows you to browse and retrieve source code for a variety of Flutter UI templates.

## Workflow

1.  **List Templates**: Use `scripts/list_templates.cjs` to see all available templates, their IDs, and descriptions.
2.  **Get Template**: Use `scripts/get_template.cjs <template-id>` to fetch the source code for a specific template.
3.  **Integrate**:
    *   Review the fetched code.
    *   Copy necessary imports.
    *   Adapt class names or styles as needed to fit the target project.
    *   Ensure required assets or fonts mentioned in the code are available.

## Bundled Resources

### Scripts
- `scripts/list_templates.cjs`: Lists all available templates from the remote manifest.
- `scripts/get_template.cjs`: Fetches the source code for a specific template ID.
