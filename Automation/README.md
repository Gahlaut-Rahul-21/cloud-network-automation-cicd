# Automation

> Status: placeholder. Demo project to be added.

Reusable automation patterns for infrastructure and network tasks: configuration generation, orchestration, scheduling and drift detection.

## Scope

- Config management and templating
- Task orchestration and scheduling
- Idempotent changes, dry runs and rollback
- Drift detection between desired and actual state
- Event-driven automation (webhooks, message queues)

## Planned demo

A "desired state" tool that renders device or server configs from YAML intent, applies them, and reports drift.

1. Describe intent in YAML (validated with a schema)
2. Render configs with Jinja2 templates
3. Dry run shows a diff, then apply with confirmation
4. Scheduled drift check produces a report
5. CLI plus a small REST API to trigger jobs

## Open-source stack

| Purpose | Tool |
|---|---|
| Configuration management | Ansible |
| Templating | Jinja2 |
| Validation | Pydantic, JSON Schema |
| Network automation | Nornir, Netmiko |
| Workflow scheduling | Prefect or Apache Airflow |
| CLI and API | Typer, FastAPI |
| Testing | pytest, molecule |

## Proposed layout

```
Automation/
├── intent/        # YAML desired-state files
├── templates/     # Jinja2 templates
├── playbooks/     # Ansible playbooks
├── src/           # Python CLI, API and drift logic
├── tests/
└── README.md
```

## Learning outcomes

- Write idempotent, testable automation
- Separate intent (what) from implementation (how)
- Detect and report configuration drift
