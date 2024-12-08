# EXTERNAL-SOURCE-LOAD

## Description


---

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* IDE used pycharm 2024.3 or later [download](https://www.jetbrains.com/pycharm/download/?section=windows)
* Python 3.13 [official doc](https://www.python.org/downloads/)
* Git version 2.47 or later [official doc](https://git-scm.com/)

### Configuration

Install requiremenets 
````bash
pip install -r requirements.txt
````

Copy and modify the .env
````bash
cp .env.example .env
````

---

## Development environment

---

## Collaborate

* Workflow
    * [Gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20est%20l'un%20des,les%20hotfix%20vers%20la%20production.)
    * [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
    * [How to use your workflow](https://nvie.com/posts/a-successful-git-branching-model/)

    * Propose a new feature in [Github issues](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)
    * Pull requests are open to merge in the develop branch.
    * Release on the main branch we use GitFlow and not with GitHub release.
    * Issues are added to the [github issues page](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)

### Commits
* [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
```bash
<type>(<scope>): <subject>
```

- **build**: Changes that affect the build system or external dependencies (e.g., npm, make, etc.).
- **ci**: Changes related to integration or configuration files and scripts (e.g., Travis, Ansible, BrowserStack, etc.).
- **feat**: Adding a new feature.
- **fix**: Bug fixes.
- **perf**: Performance improvements.
- **refactor**: Modifications that neither add a new feature nor improve performance.
- **style**: Changes that do not affect functionality or semantics (e.g., indentation, formatting, adding spaces, renaming a variable, etc.).
- **docs**: Writing or updating documentation.
- **test**: Adding or modifying tests.

examples :
```bash
chore(git): Create .gitignore
````
Complete synthaxe

```bash
feat(handler class): Update class name
<empty line>
LACK: Refactor test case with right name usage
````

---

## License
MIT

---

## Contact

* If needed you can create an issue on GitHub we will try to respond as quickly as possible.