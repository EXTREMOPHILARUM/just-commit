# Enhanced Logging

The `features/enhanced_logging.py` module provides improved logging functionalities for Git operations, enhancing the readability and filterability of log outputs.

## Overview

The Enhanced Logging feature reformats the standard Git log output to make it more readable and informative. It also allows for filtering the log based on specific keywords, making it easier to find relevant commits.

## Usage

### Formatting Log Output

The `format_log_output` method applies a custom format to the Git log output. For example, it transforms the standard commit hash display into a more readable "Commit ID: <hash>" format.

### Filtering Log

The `filter_log` method allows users to filter the Git log output by a specific keyword. This is particularly useful for quickly finding commits related to a specific feature or bug fix.

### Searching in Log

Similar to filtering, the `search_in_log` method enables searching the Git log for a specific term, providing a formatted output of relevant log entries.

## Examples

### Formatted Log Output

```python
enhanced_logging = EnhancedLogging()
print(enhanced_logging.filter_log("fix"))
```

This example demonstrates how to filter the log for commits containing the word "fix", displaying the formatted log output.

### Search in Log

```python
print(enhanced_logging.search_in_log("performance"))
```

This example shows how to search the log for the term "performance", displaying relevant, formatted log entries.

## Integration

To integrate Enhanced Logging into your workflow, instantiate the `EnhancedLogging` class and use its methods to format, filter, or search your Git log as needed.
