# Changelog Generation Documentation

## Overview

The `features/changelog_generation.py` module automates the process of generating changelog entries based on commit messages. This document outlines how to use this feature to maintain an up-to-date and informative changelog for your project.

## Generating Changelog Entries

The ChangelogGenerator class uses a machine learning model to enhance commit messages into more descriptive changelog entries. This process involves analyzing the commit message and generating a more detailed and user-friendly version of it.

### Example Usage

```python
from features.changelog_generation import ChangelogGenerator

changelog_generator = ChangelogGenerator()
last_commit_message = changelog_generator.get_last_commit_message()
changelog_entry = changelog_generator.generate_changelog_entry(last_commit_message)
changelog_generator.update_changelog(changelog_entry)
```

This code snippet demonstrates how to instantiate the ChangelogGenerator class, retrieve the last commit message, generate a changelog entry, and then update the `CHANGELOG.md` file with the new entry.

## Examples of Generated Changelog Entries

Based on different types of commit messages, the ChangelogGenerator might generate the following changelog entries:

- For a feature addition: `Added login functionality for enhanced user authentication.`
- For a bug fix: `Fixed issue where users could not log out under certain conditions.`
- For code refactoring: `Refactored user authentication flow for better performance and maintainability.`

These examples illustrate how the generated changelog entries provide a clear and concise summary of the changes, making it easier for users and contributors to understand the project's evolution.

## Conclusion

The changelog generation feature in Just Commit simplifies the process of maintaining a project's changelog by automatically generating descriptive entries from commit messages. By integrating this feature into your workflow, you can ensure that your project's changelog is always up-to-date and informative.
