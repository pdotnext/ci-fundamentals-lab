# Learning Log — CI/CD Mastery Journey

## Day 1 — [21-02-2026]

**Concept studied:** Git as a pipeline event system. The trigger contract. Conventional Commits.

**What I built:** Project scaffolding for ci-fundamentals-lab. Python app with 4 passing tests. Branch protection on main.

**Key insight:** Git is not just version control — it is the event system that every pipeline listens to. The branch name and commit message are metadata that the pipeline reads to make decisions.

**What confused me:** Github is used as event system as well, previously i used to think, it is just repositry of codes

**What I will do tomorrow:** Write the first GitHub Actions CI workflow that runs these tests automatically on every push.

**Commit SHA:** ce13f4b213557f44a830ce30ffb88a74db44454f

### Trigger contract

Today I learnt what is trigger contract. 
Trigger contract is contract you as devops engineer write so that
- Version Control System (Git)
- CI/CD pipeline

work together.
Git is event based system i.e. it always watch for specific events.
e.g. of those events are
- push request
- pull request
- tag

Once these events are trigger, git can notify Github action to do

- linting
- checks
- unit testing
- integration testing

**Without** these rules in places, pipeline can run for small and unimportant changes e.g. changes .gitignore fail
It is referred as Pipeline fatigue

### Why we need to protect main branch?

Main branch will only executed by CI/CD pipeline.
And humans can easily by pass CI/CD pipeline and bypass

- guardrails
- status checks to pass
- required reviewers

This can lead to insecure code practices, application instability by merging codes
without reviewing it.Direct merge bypasses Pull Request.
but above all it means pipeline cannot deliver on it contract and what is expectd out of it.

Conventional Commit a long term view
At this stage all commits might look over work and no one is reading them
But when in six month, you wish to roll back to most recent production release
these commit will help and save your job.
