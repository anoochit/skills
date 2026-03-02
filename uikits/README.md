# Flutter UI Kits Skill for Gemini CLI

This Gemini CLI skill enables rapid scaffolding of beautiful and functional Flutter UI components from a curated collection of templates. It allows developers to quickly browse and integrate common screens like Login, Signup, Profile, and Feed into their Flutter projects.

## Features

- **Browse Templates**: Discover a variety of pre-designed Flutter UI screens.
- **Fetch Source Code**: Instantly retrieve the Dart source code for any selected template.
- **Easy Integration**: Scaffolds code directly into your project context for quick adaptation.

## Usage

This skill is designed to be used within the Gemini CLI environment. Once activated, you can use it to:

1. **List Available Templates**:
   Gemini can browse the list of available UI kits to find one that fits your needs.
2. **Retrieve a Template**:
   Specify a template ID to get the source code, which you can then review and adapt.

### Manual Script Usage

If you need to run the underlying scripts manually from the terminal:

- **List all templates**:

  ```bash
  node scripts/list_templates.cjs
  ```

- **Get a specific template**:
  ```bash
  node scripts/get_template.cjs <template-id>
  ```

## Integration Workflow

1. **Discover**: Ask Gemini to show you available Flutter UI templates.
2. **Select**: Choose a template that matches your requirement (e.g., "Modern Login Screen").
3. **Scaffold**: Gemini will fetch the code.
4. **Refine**: Review the generated code, update imports, and style it to match your app's theme.

## Installation

To add this skill to your Gemini CLI:

1. Clone this repository or download the source.
2. Point your Gemini CLI configuration to the `SKILL.md` file in this directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
