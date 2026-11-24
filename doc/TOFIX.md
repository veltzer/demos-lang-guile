# TOFIX

Findings from a code scan on 2026-10-04.

## Low

- `rsconstruct.toml:28` - `[processor.ruff]` (and `[processor.mypy]` at `rsconstruct.toml:32`) list `src` and `config` in `src_dirs`, but those hold only `.scm` and `.lua` files; the only Python file is in `scripts/`, so set `src_dirs = ["scripts"]` for both.
- `pyproject.toml:10` - `pytest` is in the dev dependency group but the repo has no tests and no pytest processor in `rsconstruct.toml`; drop it (and refresh `uv.lock`) or add tests.
- `src/hello_world.scm:1` - the repo has a single demo (README reports "1 examples"), so it does not yet cover anything of Guile beyond hello-world; add real demos (modules, macros, continuations, FFI) or fold the repo into a broader one.
