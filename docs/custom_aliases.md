# Custom Git Aliases Documentation

## Overview

The `features/custom_aliases.py` module provides a convenient way to set up custom git aliases, enhancing the git command line experience. This document explains the setup and usage of these aliases, making git operations faster and more intuitive.

## Setup

To set up custom git aliases, run the `setup_custom_aliases` function within the `features/custom_aliases.py` module. This function iterates over a predefined list of aliases and their corresponding git commands, setting them up for use.

## Available Aliases

Below is a list of all available aliases provided by Just Commit, along with their corresponding git commands:

- `co` -> `checkout`
- `br` -> `branch`
- `cm` -> `commit`
- `st` -> `status`
- `lg` -> `log --graph --oneline --decorate --all`
- `df` -> `diff`
- `dc` -> `diff --cached`
- `ad` -> `add`
- `ps` -> `push`
- `pl` -> `pull`
- `ft` -> `fetch`
- `mg` -> `merge`
- `rb` -> `rebase`
- `cp` -> `cherry-pick`
- `stsh` -> `stash`
- `apl` -> `apply`
- `rvt` -> `revert`
- `rst` -> `reset`
- `sw` -> `switch`
- `rt` -> `remote`

## Usage

After setting up the aliases, you can use them as shortcuts for their corresponding git commands. For example, instead of typing `git checkout`, you can simply type `git co`.

## Conclusion

Custom git aliases are a powerful way to streamline your git workflow. By using the aliases provided by Just Commit, you can perform git operations more efficiently and with less typing.
