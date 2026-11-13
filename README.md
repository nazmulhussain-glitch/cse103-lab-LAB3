# CSE103 Lab 3 — GitHub Collaboration & API Interaction

**Student:** Nazmul Hussain  
**GitHub:** [nazmulhussain-glitch](https://github.com/nazmulhussain-glitch)  
**Repository:** [cse103-lab-LAB3](https://github.com/nazmulhussain-glitch/cse103-lab-LAB3)  
**Course:** CSE103

---

## 1. Overview

This repository contains practical work for CSE103 Lab 3. It demonstrates the basic Git workflow, creating and managing a GitHub repository, tracking changes with commits, writing project documentation in Markdown, identifying common errors, and accessing structured information from a public JSON API using Python.

The project is organised into small files so that each concept can be understood and reviewed separately. The Python examples are intentionally beginner-friendly and include comments, readable names, and basic error handling.

## 2. Learning objectives

After reviewing this project, a student should be able to:

- Explain what a Git repository is and why version control is useful.
- Create a repository and organise project files.
- Track changes and save meaningful commits.
- Push local project changes to GitHub and understand the purpose of pulling updates.
- Write structured documentation using Markdown headings, lists, links, code blocks, and tables.
- Recognise common programming and Git workflow errors.
- Send a request to a public API and understand the JSON data returned.
- Extract selected fields from JSON objects and save data to a file.
- Write a simple unit test for a Python function.

## 3. Project structure

```text
CSE103-LAB3/
├── README.md
├── .gitignore
├── CHANGELOG.md
├── MARKDOWN_GUIDE.md
├── main.py
├── api_client.py
├── sample_users.json
└── tests/
    └── test_api_client.py
```

### File descriptions

| File or folder | Purpose |
|---|---|
| `README.md` | Main project introduction, instructions, and lab coverage |
| `.gitignore` | Prevents temporary and generated files from being tracked |
| `CHANGELOG.md` | Records the main project updates |
| `MARKDOWN_GUIDE.md` | Demonstrates common Markdown formatting |
| `main.py` | Runs a simple greeting and project-information example |
| `api_client.py` | Requests user data from a public API and processes JSON |
| `sample_users.json` | Small sample dataset for understanding JSON structure |
| `tests/` | Contains automated tests for the API helper function |

## 4. Requirements

- Python 3.9 or newer.
- A code editor such as Visual Studio Code or any text editor.
- Git and a GitHub account for version-control practice.
- An internet connection when making the live API request.

The greeting program and unit test do not require an internet connection. The API client uses Python's standard library, so no additional Python package is required.

## 5. Run the Python examples

Open a terminal in the project directory and run:

```bash
python main.py
```

Expected output:

```text
Hello, Nazmul Hussain! Welcome to CSE103 Lab 3.
Repository: cse103-lab-LAB3
Topics: Git, GitHub, Markdown, debugging, and APIs.
```

To request live user data from JSONPlaceholder, run:

```bash
python api_client.py
```

The program requests the public `/users` endpoint, checks the response, displays selected user details, and saves the raw response to `users.json`. The generated `users.json` file is ignored by Git because it is an output file.

If the network is unavailable or the server returns an error, the program displays an error message instead of stopping with an unexplained traceback.

## 6. Run the unit test

Run the test from the project directory:

```bash
python -m unittest discover -s tests -v
```

The test checks that `summarize_users()` extracts the expected ID, name, and city from a sample user record. It uses Python's built-in `unittest` framework.

## 7. Git and GitHub workflow

A typical version-control workflow is:

```bash
git status
git add .
git commit -m "Describe the change"
git push
```

- `git status` displays changed and untracked files.
- `git add .` stages project changes for the next commit.
- `git commit` saves a snapshot with a descriptive message.
- `git push` uploads local commits to the remote GitHub repository.

A developer can use `git pull` to download and integrate updates from the remote repository. Meaningful commit messages make the project history easier to understand.

## 8. Lab question coverage

| Question | Topic | Evidence in this repository |
|---|---|---|
| Q3.1 | Create and manage Git repositories | Repository structure and Git ignore rules |
| Q3.2 | Track and commit changes | Version-control workflow and commit history |
| Q3.3 | Push projects to GitHub | Public GitHub repository and push workflow |
| Q3.4 | Create Markdown documentation | This README and `MARKDOWN_GUIDE.md` |
| Q3.5 | Access public APIs and analyse JSON | `api_client.py` and `sample_users.json` |
| Q3.6 | Debug common programming and workflow errors | Error handling, troubleshooting notes, and unit test |

## 9. API and data notes

The live API example uses JSONPlaceholder, a public testing API. The `sample_users.json` file is a small illustrative dataset included to make the JSON structure easy to inspect. It is not represented as a newly downloaded live response. Running `api_client.py` creates a separate `users.json` file containing the response received at runtime.

## 10. Author

**Nazmul Hussain**  
CSE103 — Lab 3  
GitHub: [nazmulhussain-glitch](https://github.com/nazmulhussain-glitch)
