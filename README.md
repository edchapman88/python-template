### Recommended linter and formatter:

- [Ruff](https://github.com/astral-sh/ruff), also available as a VSCode
  extension.
- Ruff config in `pyproject.toml` under `[tool.ruff]`.
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

### MyPy type checking

- `mypy` must be installed (eg. globally with pip)
- The VSCode extension (`Mypy` by Matan Gover, which is better than the
  Microsoft `Mypy Type Checker` extension) will run a server to do live type
  checking.
- Config in `pyproject.toml` under `[tool.mypy]` (it's set up to leave entirely
  un-annotated functions un-checked).
