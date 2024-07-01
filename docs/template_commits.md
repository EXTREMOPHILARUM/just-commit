# Template Commits Documentation

## Overview

The `features/template_commits.py` module provides a structured approach to generating commit messages. It offers predefined templates for different types of commits, such as features, bug fixes, and refactorings. This ensures consistency and clarity in commit messages across the project.

## Available Templates

The module defines templates for the following commit types:

- **Feature**: For new features added to the project.
- **Bug Fix**: For bug fixes.
- **Refactor**: For code refactoring.

## Usage

To generate a commit message, specify the commit type and provide the necessary details as arguments. The module will then return a formatted commit message based on the selected template.

### Example Usage

```python
from features.template_commits import CommitTemplateGenerator

generator = CommitTemplateGenerator()
print(generator.generate_commit_message("feature", description="Add login functionality", details="Implemented login with email and password."))
print(generator.generate_commit_message("bug_fix", issue="Login button crash", resolution="Fixed null pointer exception on login."))
print(generator.generate_commit_message("refactor", scope="Login flow", reasoning="Improved code readability and performance."))
```

## Customizing Templates

The templates can be customized to fit the project's needs. To add a new template or modify an existing one, edit the `templates` dictionary in the `CommitTemplateGenerator` class.

## Conclusion

The template commits feature streamlines the process of creating commit messages, promoting consistency and clarity. By using predefined templates, developers can ensure that their commit messages are informative and follow the project's standards.
