# ci-fundamentals-lab

[![CI Pipeline](https://github.com/pdotnext/ci-fundamentals-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/pdotnext/ci-fundamentals-lab/actions)

> 90-day DevSecOps learning journey — Portfolio Project 1

## What This Repository Demonstrates

A production-grade CI pipeline built from first principles. This is not a tutorial copy-paste — every stage was designed, broken, debugged, and documented as part of a structured learning journey.

## Pipeline Architecture
```
commit → lint → test → coverage gate → build → notify
```

*(Diagram will be added as pipeline evolves)*

## Project Structure
```
ci-fundamentals-lab/
├── src/           # Application source code
├── tests/         # Automated test suite
├── .github/
│   └── workflows/ # CI/CD pipeline definitions
├── docs/          # Architecture decisions and runbooks
└── LEARNING_LOG.md
```

## Learning Log

See [LEARNING_LOG.md](./LEARNING_LOG.md) for the day-by-day journey.

## Skills Demonstrated

- [ ] CI Pipeline Design (GitHub Actions)
- [ ] Test Automation with coverage gates
- [ ] Conventional Commits & branch strategy
- [ ] Docker/Podman containerization
- [ ] Artifact management
