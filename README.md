### Recommended linter and formatter:

- [Ruff](https://github.com/astral-sh/ruff), also available as a VSCode
  extension.
- Linting and format-on-save are available by adding the following to VSCode
  `settings.json` once the extension is installed:

```
"[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
```

- `settings.json` can be accessed by searching for
  `Preferences: Open User Settings (JSON)` in the VSCode command palette.

### Pre-commit hook

- Check `pre-commit` is installed:

```bash
pre-commit --version
```

- If not installed:

```bash
brew install pre-commit
```

- Generate the git hooks script from the `.pre-commit-config.yaml` file:

```bash
pre-commit install
```
