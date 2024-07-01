def setup_custom_aliases():
    aliases = {
        'co': 'checkout',
        'br': 'branch',
        'cm': 'commit',
        'st': 'status',
        'lg': 'log --graph --oneline --decorate --all',
        'df': 'diff',
        'dc': 'diff --cached',
        'ad': 'add',
        'ps': 'push',
        'pl': 'pull',
        'ft': 'fetch',
        'mg': 'merge',
        'rb': 'rebase',
        'cp': 'cherry-pick',
        'stsh': 'stash',
        'apl': 'apply',
        'rvt': 'revert',
        'rst': 'reset',
        'sw': 'switch',
        'rt': 'remote'
    }

    for alias, command in aliases.items():
        print(f"Setting up alias: git {alias} -> git {command}")
        # This is a placeholder for the actual command to set up git aliases
        # In a real scenario, this would involve running a shell command like:
        # subprocess.run(f"git config --global alias.{alias} {command}", shell=True)

if __name__ == "__main__":
    setup_custom_aliases()
