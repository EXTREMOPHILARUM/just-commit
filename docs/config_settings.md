# Configuration Settings Documentation

## Overview

The `config/settings.py` module in the Just Commit tool is designed to manage configuration settings for the application. It allows users to enable or disable features by modifying the `config/settings.json` file. This document provides a comprehensive guide on how to use and modify these settings to customize your Just Commit experience.

## Usage

To modify the settings, navigate to the `config/settings.json` file. This file contains a JSON object where each key represents a feature within Just Commit, and the value (`true` or `false`) indicates whether the feature is enabled or disabled.

### Example Configuration

```json
{
  "intelligent_branch_naming": true,
  "enhanced_diff": false
}
```

In the example above, the `intelligent_branch_naming` feature is enabled, allowing Just Commit to suggest meaningful branch names based on the purpose of the branch. Conversely, the `enhanced_diff` feature is disabled, meaning the default git diff output will be used instead of the enhanced version provided by Just Commit.

## Enabling or Disabling Features

To enable a feature, set its corresponding value in `config/settings.json` to `true`. To disable a feature, set the value to `false`. After making changes, save the file. The next time you use Just Commit, it will read these settings and enable or disable features accordingly.

### Steps to Modify Settings

1. Open `config/settings.json` in your preferred text editor.
2. Locate the feature you wish to modify.
3. Change the value to `true` (to enable) or `false` (to disable).
4. Save the file.

## Example Usage in `config/settings.py`

The `SettingsManager` class in `config/settings.py` is responsible for loading these settings and providing an interface to access and modify them. Here is an example of how it is used:

```python
from config.settings import SettingsManager

settings_manager = SettingsManager()
if settings_manager.get_feature_status('intelligent_branch_naming'):
    print("Intelligent branch naming is enabled.")
else:
    print("Intelligent branch naming is disabled.")
```

This example checks if the `intelligent_branch_naming` feature is enabled and prints a message accordingly.

## Conclusion

The `config/settings.py` module and `config/settings.json` file provide a flexible way to customize the Just Commit tool according to your preferences. By understanding how to modify these settings, you can tailor the tool to better fit your workflow.
