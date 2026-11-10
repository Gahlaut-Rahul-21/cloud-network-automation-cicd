# CI-CD demo: Network Automation API

A small Flask service with subnet/CIDR helpers, wrapped in a full CI/CD pipeline built only from open-source tools.

| Stage | Tool |
|---|---|
| Lint / format | [Ruff](https://github.com/astral-sh/ruff) |
| Unit tests + coverage | pytest, pytest-cov |
| SAST | Bandit |
| Dependency audit | pip-audit |
| Container build | Docker |
| Image scan | Trivy |
| Deploy | Ephemeral Docker container (swap for k8s/VM in real use) |
| Post-deploy validation | `scripts/smoke_test.py` |
| Orchestration | GitHub Actions (`../.github/workflows/ci-cd-demo.yml`) |

## API

| Endpoint | Example |
|---|---|
| `GET /health` | |
| `GET /subnet?cidr=10.0.0.0/24` | subnet details |
| `GET /overlap?a=10.0.0.0/16&b=10.0.1.0/24` | overlap check |
| `GET /split?cidr=10.0.0.0/24&prefix=26` | split into subnets |

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
make install
make all          # lint, test, scan, docker build
make run && make smoke
docker stop netauto-api
```

Dev server without Docker: `flask --app app.main run --port 8000`.

## Pipeline flow

`lint-test` (py3.11/3.12) + `security` → `build-deploy-validate` (build → Trivy scan → deploy → smoke test).
