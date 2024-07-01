# Just commit

Just Commit is a Python-based CLI tool designed to enhance the git command line experience by offering a suite of features both with and without LLM integration. Leveraging the llama-cpp-python library for LLM capabilities, it aims to streamline and improve your git workflow.

## Features with LLM Integration

1. **Commit Message Suggestion**: Automatically generate or improve commit messages based on the code changes.
2. **Code Review Suggestions**: Provide inline code review suggestions.
3. **Intelligent Branch Naming**: Suggest meaningful branch names based on the purpose of the branch.
4. **Automated Changelog Generation**: Generate a changelog entry for each commit or release.
5. **Interactive Rebase Assistant**: Assist with interactive rebases.
6. **Conflict Resolution Assistance**: Provide suggestions for resolving merge conflicts.
7. **Documentation Updates**: Automatically suggest updates to documentation based on code changes.

## Features without LLM Integration

1. **Enhanced Git Diff**: Provide a more detailed git diff output.
2. **Pre-Commit Checks**: Integrate pre-commit hooks to enforce code standards.
3. **Custom Aliases and Shortcuts**: Provide custom git aliases and shortcuts.
4. **Template Commits**: Offer commit message templates for different types of commits.
5. **Enhanced Logging**: Improve the git log output.
6. **Bulk Operations**: Simplify bulk operations like mass branch deletion.
7. **Interactive Rebase Tool**: Create an interactive tool to assist with rebases.
8. **Backup and Recovery**: Implement automatic backup and recovery options.
9. **Enhanced Merge Tool**: Provide a more intuitive merge tool.
10. **Visual Git Status**: Display a graphical representation of the git status.

## Configuration

Users can enable or disable LLM features through a configuration file. This enhances customization and allows for a tailored git experience. The configuration file is located at `config/settings.json` and follows the JSON format. Each LLM feature can be toggled on or off individually.

## Initial Setup and Configuration

For an easy first setup and an overview of all configurations, users are guided to the sample configuration file provided at `config/sample_settings.json`. This sample file demonstrates all configurable features with default settings, allowing users to quickly start with a pre-configured set of features. To use it, simply copy `config/sample_settings.json` to `config/settings.json`.

## Examples

- **Branch Names**: `feature/add-login`, `bugfix/resolve-crash`, `refactor/improve-performance`
- **Changelog Entry**: `Added login functionality for enhanced user authentication. Includes error handling and state management improvements.`

## Installation and Usage

To install and use Just Commit as a Python package, follow these steps:

1. Ensure Python 3.8 or higher is installed on your system.
2. Clone the repository and navigate to the project directory.
3. Install the package using `pip install .`.
4. Import and use the package modules in your Python scripts as needed.

For more detailed instructions and examples, refer to the documentation in the `docs` folder.

## GitHub Actions Integration

Just Commit now supports GitHub Actions, allowing you to automate your workflows directly from GitHub. This integration enables you to run tests, package your tool, and more, right from your GitHub repository.

### Example GitHub Actions Workflow

Below is an example of a GitHub Actions workflow file that you can use to set up your CI/CD pipeline with Just Commit. This workflow installs dependencies, runs tests, and packages the tool.

```yaml
name: Just Commit CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
    - name: Package tool
      run: |
        python setup.py sdist bdist_wheel
```

This workflow is triggered on every push and pull request to the repository. It uses Python 3.8 for running the actions and includes steps for checking out the code, setting up Python, installing dependencies, running tests, and packaging the tool.

## Detailed Feature Documentation

For comprehensive documentation on each feature, including usage examples, integration guidelines, and more, please visit the `docs` folder. Each component's documentation includes a link back to its source code for easy reference, ensuring a seamless navigation between documentation and implementation.
