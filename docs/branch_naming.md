# Branch Naming Documentation

## Overview

The `features/branch_naming.py` module provides intelligent suggestions for branch names based on the changes made in the working directory. This document outlines how to use this feature to generate meaningful branch names that reflect the purpose of the changes.

## Suggested Branch Naming

The BranchNamer class uses a machine learning model to analyze the changes and suggest a branch name that summarizes the changes' intent. This process involves generating a text suggestion based on the diff and then formatting it to fit branch naming conventions (e.g., lowercase letters and underscores).

### Example Usage

```python
from features.branch_naming import BranchNamer

branch_namer = BranchNamer()
changes = branch_namer.get_git_changes()
suggested_branch_name = branch_namer.suggest_branch_name(changes)
print(f"Suggested branch name: {suggested_branch_name}")
```

This code snippet demonstrates how to instantiate the BranchNamer class, retrieve the current git changes, and then generate a suggested branch name.

## Examples of Suggested Branch Names

Based on different types of changes, the BranchNamer might suggest the following branch names:

- For a feature addition: `feature_add_login_functionality`
- For a bug fix: `fix_login_button_crash`
- For code refactoring: `refactor_improve_login_performance`

These examples illustrate how the suggested branch names clearly reflect the nature of the changes, making it easier for team members to understand the purpose of each branch at a glance.

## Conclusion

The branch naming feature in Just Commit simplifies the process of naming branches by providing meaningful, context-based suggestions. By following the usage examples and integrating this feature into your workflow, you can ensure that your branch names are consistently descriptive and informative.
