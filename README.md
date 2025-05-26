### Simple Flask App with Github Action 

**GitHub** is a cloud-based platform built around Git (version control system), used for:

- Hosting repositories (code)
- Collaborating via pull requests and issues
- Managing project version history
- Integrating CI/CD with GitHub Actions
- Publishing documentation or static sites via GitHub Pages

###### Key GitHub Concepts

**Concept**	Explanation
**Repository**	A project folder with version history, hosted on GitHub
**Branch**	A separate line of development (e.g., main, dev, feature-x)
**Commit**	A saved change to the codebase
**Pull** Request (PR)	A request to merge changes from one branch to another
**Issues**	Used to track bugs, features, tasks
**Fork**	A copy of someone else's repo that you can modify independently
**GitHub Pages**	Hosts static websites from a GitHub repo
**GitHub Actions**	Built-in CI/CD system to automate workflows like build, test, deploy

###### GITHUB ACTIONS

**GitHub Actions** is GitHub's CI/CD (Continuous Integration/Deployment) feature.

- Automate tasks when events happen in your repo (like push, PR, release)
- Run tests, build code, or deploy to cloud platforms
- Create reusable workflows (YAML files)

###### Key Concepts in GitHub Actions:

**Workflow**	The automation you define (written in .github/workflows/*.yml)
**Job**	A group of steps that run on the same runner
**Step**	A single task (e.g., checkout repo, run Python script)
**Runner**	The machine that runs your workflow (ubuntu-latest, windows, etc.)
**Event**	What triggers the workflow (e.g., push, pull_request)
**Action**	A prebuilt piece of functionality (e.g., actions/checkout)

###### Sample Workflow File

```bash
# .github/workflows/python-app.yml
name: Python Flask CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run Tests
      run: pytest
```

###### GITHUB & ACTIONS INTERVIEW QUESTIONS

