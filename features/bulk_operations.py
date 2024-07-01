import subprocess

class BulkOperations:
    def __init__(self):
        pass

    def delete_branches(self, branches):
        for branch in branches:
            subprocess.run(['git', 'branch', '-D', branch])

    def merge_branches(self, target_branch, branches):
        subprocess.run(['git', 'checkout', target_branch])
        for branch in branches:
            subprocess.run(['git', 'merge', branch])

    def stash_changes_bulk(self):
        subprocess.run(['git', 'stash', 'push', '--all'])

if __name__ == "__main__":
    bulk_ops = BulkOperations()
    # Example usage:
    # bulk_ops.delete_branches(['feature/old-feature', 'bugfix/old-bugfix'])
    # bulk_ops.merge_branches('develop', ['feature/new-feature', 'bugfix/new-bugfix'])
    # bulk_ops.stash_changes_bulk()
