# Repository Guidelines

## Project Structure & Module Organization

This repository currently contains project documentation for a PPE detection initiative in construction safety. The main project overview is in `README.md`; repository-wide text normalization is configured in `.gitattributes`.

When implementation is added, keep the layout predictable:

- `src/` for application code, model pipelines, and reusable modules.
- `tests/` for automated tests that mirror `src/` module names.
- `data/` for small sample metadata only; do not commit large datasets.
- `assets/` or `docs/` for diagrams, sample images, and supporting documentation.
- `models/` for model configuration or lightweight metadata, not large trained weights.

## Build, Test, and Development Commands

No build system, package manager, or test runner is configured yet. Until one is added, validate documentation changes manually and check repository status before submitting:

```sh
git status --short
```

When code is introduced, document the exact setup and workflow commands in `README.md`, for example `python -m pytest`, `npm test`, or `make build`.

## Coding Style & Naming Conventions

Use clear, domain-specific names related to construction safety and PPE detection, such as `helmet_detector`, `vest_compliance`, or `ppe_violation_report`. Prefer small modules with single responsibilities.

For Markdown, use sentence-case headings, concise paragraphs, and hyphen bullets. Keep lines readable and avoid committing generated files unless they are required project artifacts. The repository uses LF normalization through `.gitattributes`.

## Testing Guidelines

There are no tests yet. Add tests with the first implementation change. Place them under `tests/` and name them after the behavior or module being verified, such as `test_ppe_labels.py` or `test_detection_pipeline.py`.

For computer vision work, include tests for data parsing, label mapping, confidence thresholds, and edge cases such as missing PPE classes or empty detections. Avoid tests that require large local datasets unless fixtures are small and committed intentionally.

## Commit & Pull Request Guidelines

Existing commits use short, imperative messages, for example `Add README with project overview and objectives`. Continue that style: start with a verb, keep the subject concise, and describe one logical change per commit.

Pull requests should include a brief summary, the reason for the change, validation performed, and any dataset/model assumptions. For visual or model-behavior changes, include representative examples, metrics, or screenshots where practical.

## Security & Configuration Tips

Do not commit credentials, private image datasets, trained model binaries, or environment-specific paths. Use ignored local configuration files for secrets and document required variables in the README when they are introduced.
