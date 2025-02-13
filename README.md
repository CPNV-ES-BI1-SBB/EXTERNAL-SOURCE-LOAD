# EXTERNAL-SOURCE-LOAD

## Description

This project is designer to load data from external source to a DataWarehouse and the main features are :
- Expose an api route to get data from external source
- Transform the data to Python Object
- Transform Python Object to Sql normalized queries that can be loaded to a DataWarehouse
- 
## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* IDE used pycharm 2024.3 or later [download](https://www.jetbrains.com/pycharm/download/?section=windows)
* Python 3.13 [official doc](https://www.python.org/downloads/)
* Pipenv version 2024.4.1 [official doc](https://pipenv.pypa.io/en/latest/)
* Git version 2.47 or later [official doc](https://git-scm.com/)

### Configuration

Indicate to Jetbrains your python interpreter for this project
````bash
Settings | Project: EXTERNAL-SOURCE-LOAD | Python Interpreter
````

Install requirements 
````bash
pipenv shell
pipenv install
````

Copy and modify the .env.exemple
````bash
cp .env.exemple .env
````

Run the tests
````bash
pytest <name of the test file>
````
Run the service
````bash
fastapi run
````
## Directory structure

```shell
.EXTERNAL-SOURCE-LOAD
├── app                           // Classes and packages
│   ├── helpers             // Helpers functions
│   ├── providers           // Providers to connect to external source
│   └── utils               // Utils functions
├── docs
│   └── diagram
└── tests                         // Tests classes
````

## Collaborate

   * [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
   * Propose a new feature in [Github issues](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD/issues)
   * Pull requests are open to merge in the develop branch.
   * Issues are added to the [github issues page](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD/issues)

### Commits
```bash
<type>(<scope>): <subject>
```

- **build**: Changes that affect the build system or external dependencies (e.g., npm, make, etc.).
- **ci**: Changes related to integration or configuration files and scripts (e.g., Travis, Ansible, BrowserStack, etc.).
- **feat/feature**: Adding a new feature.
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
Complete syntax with scope, body and footer

```bash
feat(handler class): Update class name
<empty line>
The class wasn't in line with the class diagram
<empty line>
LACK: Refactor test case with right name usage
````
Both the body and footer are optional.

## License
MIT

## Contact

* If needed you can create an issue on GitHub we will try to respond as quickly as possible.
