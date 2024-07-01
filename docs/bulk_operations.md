# Bulk Operations Documentation

## Overview

The `features/bulk_operations.py` module provides functionality for performing bulk operations on branches, such as deleting and merging multiple branches at once. This document outlines how to use these operations to manage branches efficiently.

## Deleting Branches

To delete multiple branches in a single operation, the `delete_branches` method is used. This method takes a list of branch names as input and deletes each branch.

### Usage Example

```python
from features.bulk_operations import BulkOperations

bulk_ops = BulkOperations()
bulk_ops.delete_branches(['feature/old-feature', 'bugfix/old-bugfix'])
```

This code snippet demonstrates how to delete two branches named `feature/old-feature` and `bugfix/old-bugfix`.

## Merging Branches

To merge multiple branches into a target branch, the `merge_branches` method is used. This method first checks out the target branch, then merges each branch in the list into the target branch.

### Usage Example

```python
from features.bulk_operations import BulkOperations

bulk_ops = BulkOperations()
bulk_ops.merge_branches('develop', ['feature/new-feature', 'bugfix/new-bugfix'])
```

This code snippet demonstrates how to merge two branches named `feature/new-feature` and `bugfix/new-bugfix` into the `develop` branch.

## Stashing Changes in Bulk

The `stash_changes_bulk` method allows for stashing all changes in the working directory in a single operation. This is useful for quickly saving work in progress before switching branches.

### Usage Example

```python
from features.bulk_operations import BulkOperations

bulk_ops = BulkOperations()
bulk_ops.stash_changes_bulk()
```

This code snippet demonstrates how to stash all changes in the working directory.

## Conclusion

The bulk operations provided by `features/bulk_operations.py` are essential for managing branches efficiently in a repository. By following the usage examples, you can streamline your branch management process.
