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

Local workspace checking:

- `mypy` must be installed (eg. globally with pip)
- The VSCode extension (`Mypy` by Matan Gover, which is better than the
  Microsoft `Mypy Type Checker` extension) will run a server to do live type
  checking **of the entire workspace**, not just files that have changes.
- Config in `pyproject.toml` under `[tool.mypy]` (it's set up to leave any
  entirely un-annotated functions un-checked, to provide good type checking
  whilst allowing for partial type coverage).
- `[[tool.mypy.overrides]]` sections in `pyproject.toml` allow for module
  specific settings, or applying a set of settings to a list of modules - eg. to
  blacklist a set of modules that do not have type support and are to be ignored
  by mypy.

Pre-commit checking:

- The pre-commit hook **will only type check files that have changed**, so is
  not as strict as the local type checking with the VSCode extension (mypy
  daemon).
- If an external module **does have** type support, it should **not** be
  blacklisted, and instead the **dependency must be added to the
  `.pre-commit-config.yaml` file**, under `additional_dependencies` for the mypy
  hook.
- The mypy pre-commit checks are run **in a seperate** python environment,
  without the modules that have been installed into the project working
  envionment. This is the reason that the pre-commit hook needs to be aware of
  the 3rd-party modules that do have type support, and for which type stubs must
  be fetched.
